#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool,Int32
import numpy as np
import math
from enum import Enum

RAD2DEG = 180 / math.pi

# OBJECTIVES
# Identify Range of lidar (30,15,5,2) in meter
# STATE NAVIGATION MODE (Moving,Obsctacle ahead, Nearing Obstacle,SOS Breaking)
# Reduce Spead while nearing obstacle 
#
# TO-DO
# Notify Obstacl while turning left/right
#
#
#
#
class ObstacleState(Enum):
	NONE = 0
	MOVING = 1
	OBSTACLE_AHEAD = 2
	NEARING_OBSTACLE = 3
	SOS_BREAKING = 4

class ObstacleAvoidance(Node):

	def __init__(self):
		super().__init__('ObstacleAvoidance')

		self.obstacle_state = ObstacleState.NONE

		self.subscription = self.create_subscription(LaserScan, 'front_scan', self.scan_callback, 10)
		self.publisher = self.create_publisher(Twist, 'cmd_vel', 5)
		self.ctrl_state_publisher = self.create_publisher(Bool, 'controler_state', 10)
		self.obstacle_state_pub = self.create_publisher(Int32, 'obstacle_state', 10)
		
		# minimum distance for breaking
		self.declare_parameter("min_obstacle_distance",0.5)
		self.minimum_distance = self.get_parameter('min_obstacle_distance').get_parameter_value().double_value
		# maxmimum distance for identification
		self.declare_parameter("max_obstacle_distance",0.7)
		self.max_obstacle_distance = self.get_parameter('max_obstacle_distance').get_parameter_value().double_value
		# sos minimum distance for breaking
		self.declare_parameter("sos_distance",0.3)
		self.sos_distance = self.get_parameter('sos_distance').get_parameter_value().double_value


	def scan_callback(self, scan_data):
		if not isinstance(scan_data, LaserScan): return
		self.setObstacleState(scan_data)
		ctrl_state = Bool()
		ctrl_state.data = True
		self.ctrl_state_publisher.publish(ctrl_state)
		# publish obstacle state
		obstacle_state_value = Int32()
		obstacle_state_value.data = self.obstacle_state.value
		self.obstacle_state_pub.publish(obstacle_state_value)
	
	def setObstacleState(self,scan_data):
		l1_right_data = np.array(scan_data.ranges[0:224])
		l1_front_right_data = np.array(scan_data.ranges[225:449])
		l1_front_left_data = np.array(scan_data.ranges[450:674])
		l1_left_data = np.array(scan_data.ranges[675:897])
		
		# FRONT ONLY
		# Emergency stop on sudden obstacle and nearing obstacle to reduce speed
		if l1_front_left_data[l1_front_left_data < self.sos_distance].any():
			self.obstacle_state = ObstacleState.SOS_BREAKING
			self.obstacleFound()
		elif l1_front_right_data[l1_front_right_data < self.sos_distance].any():
			self.obstacle_state = ObstacleState.SOS_BREAKING
			self.obstacleFound()
		elif l1_front_left_data[l1_front_left_data < self.minimum_distance].any():
			self.obstacle_state = ObstacleState.NEARING_OBSTACLE
		elif l1_front_right_data[l1_front_right_data < self.minimum_distance].any():
			self.obstacle_state = ObstacleState.NEARING_OBSTACLE
		elif l1_front_left_data[l1_front_left_data < self.max_obstacle_distance].any():
			self.obstacle_state = ObstacleState.OBSTACLE_AHEAD
		elif l1_front_right_data[l1_front_right_data < self.max_obstacle_distance].any():
			self.obstacle_state = ObstacleState.OBSTACLE_AHEAD
		else:
			self.obstacle_state = ObstacleState.MOVING
		
	def obstacleFound(self):
		move = Twist()
		ctrl_state = Bool()
		ctrl_state.data = False
		self.ctrl_state_publisher.publish(ctrl_state)
		move.linear.x = 0.0
		self.publisher.publish(move)	

def main(args=None):
	rclpy.init(args=args)
	obstacle_avoidance = ObstacleAvoidance()
	rclpy.spin(obstacle_avoidance)
	obstacle_avoidance.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
