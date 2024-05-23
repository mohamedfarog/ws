#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, TransformStamped
from nav_msgs.msg import Path
from sensor_msgs.msg import LaserScan
import tf2_ros
import math

import rclpy
from rclpy.clock import Clock
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import numpy as np
import math
from laser_geometry import LaserProjection
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2

class laserscanToPointPublish(Node):

    def __init__(self):
        super().__init__('robot_pose_publisher')
        self.subscription = self.create_subscription(LaserScan,'/combined_scan',self.laserscan_callback,10)
        self.sacn_point_publisher = self.create_publisher(PointCloud2,'/scan_points',10)
        
    def laserscan_callback(self, msg):
        if not isinstance(msg, LaserScan): return
        
        ranges = msg.ranges
        angle_min = msg.angle_min
        angle_increment = msg.angle_increment

        pc_data = []
        for i, range_value in enumerate(ranges):
            if not math.isinf(range_value):
                # Calculate Cartesian coordinates
                angle = angle_min + i * angle_increment
                x = range_value * math.cos(angle)
                y = range_value * math.sin(angle)
                z = 0.0  # Assuming a 2D LaserScan, set z-coordinate to 0

                # Append point to PointCloud data
                pc_data.append([x, y, z])
       
        header = msg.header
        pc_msg = pc2.create_cloud_xyz32(header, pc_data)
        self.sacn_point_publisher.publish(pc_msg)
        # print("asdasdas")
        
            
    def laserscan_to_points(self, laserscan, angle_min, angle_increment):
        points = []
        angle = angle_min
        laser_points = Path()

        for distance in laserscan:
            x = distance * math.cos(angle)
            y = distance * math.sin(angle)
            pose = PoseStamped()
            pose.pose.position.x = x
            pose.pose.position.y = y
            points.append(pose)
            angle += angle_increment
        laser_points.poses = points
 
        return laser_points


def main(args=None):
    rclpy.init(args=args)

    robot_laser_scan_publisher = laserscanToPointPublish()

    rclpy.spin(robot_laser_scan_publisher)

    robot_pose_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
