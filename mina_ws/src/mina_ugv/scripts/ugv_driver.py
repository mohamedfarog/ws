#!/usr/bin/env python3
# encoding: utf-8

#public lib
import sys
import math
import random
import threading
from math import pi
from time import sleep

#ros lib
import rclpy
from rclpy.node import Node
from std_msgs.msg import String,Float32,Int32,Bool
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu,MagneticField, JointState
from rclpy.clock import Clock

class Dism_driver(Node):
	
	def __init__(self, name):
		super().__init__(name)

		print("Dism_driver")
		self.get_logger().info(" DRIVER STARTED")

		#create subcriber
		# self.sub_cmd_vel = self.create_subscription(Twist,"cmd_vel",self.cmd_vel_callback,1)
		
		#create publisher
		self.statePublisher = self.create_publisher(JointState,"joint_states",100)
		# self.velPublisher = self.create_publisher(Twist,"vel_raw",50)
		
		#create timer
		self.timer = self.create_timer(0.1, self.pub_data)

	
	def pub_data(self):
		time_stamp = Clock().now()
		twist = Twist()
		state = JointState()
		state.header.stamp = time_stamp.to_msg()
		state.header.frame_id = "joint_states"
		state.name = ["back_right_joint", "back_left_joint","front_left_steer_joint","front_left_wheel_joint",
							"front_right_steer_joint", "front_right_wheel_joint"]
		
		vx, vy, angular = 1.0,1.0,1.0
		twist.linear.x = vx*1.0    #velocity in axis 
		twist.linear.y = vy*1000*1.0   #steer angle
		twist.angular.z = angular*1.0    #this is invalued
		
		# self.velPublisher.publish(twist)
		
		#turn to radis
		steer_radis = vy*1000.0*3.1416/180.0
		state.position = [0.0, 0.0, steer_radis, 0.0, steer_radis, 0.0]
		if not vx == angular == 0:
			i = random.uniform(-3.14, 3.14)
			state.position = [i, i, steer_radis, i, steer_radis, i]
		self.statePublisher.publish(state)
			
def main():
	rclpy.init() 
	driver = Dism_driver('dism_driver')
	rclpy.spin(driver)
		
if __name__ == "__main__":
    main()
		
