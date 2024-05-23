#!/usr/bin/env python3

import rclpy
from rclpy.clock import Clock
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import numpy as np
import math
import copy
from std_msgs.msg import Float32MultiArray

RAD2DEG = 180 / math.pi
scann = LaserScan()

class LidarScanCustomNode(Node):

    def __init__(self):
        super().__init__('LidarScan')

        self.combined_laser = LaserScan()
        self.front_laser = LaserScan()
        self.back_laser = LaserScan()

        self.subscription = self.create_subscription(LaserScan, 'front_lidar', self.front_lidar_callback, 10)
        self.front_laser_publisher = self.create_publisher(LaserScan,"front_scan",10)
        self.backLidarsub = self.create_subscription(LaserScan, 'back_lidar', self.back_lidar_callback, 10)
        self.back_laser_publisher = self.create_publisher(LaserScan,"back_scan",10)
        self.combained_laser_publisher = self.create_publisher(LaserScan,"combined_scan",10)

        self.timer = self.create_timer(0.1, self.create_combined_scandata)
    
    def create_combined_scandata(self):
        total_range = len(self.front_laser.ranges)
        average_separation = total_range / 8

        # #0-44
        # l1_front_left_data = np.array(self.front_laser.ranges[0:int(average_separation - 1)]) 
        # #45-89
        # l1_left_data = np.array(self.front_laser.ranges[int(average_separation):int(average_separation*2)])
        # #90-134
        # l2_right_data = np.array(self.back_laser.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
        # #135-179
        # l2_front_right_data = np.array(self.back_laser.ranges[int(total_range + average_separation):int(total_range - 1)])
        # #180 -224
        # l2_front_left_data = np.array(self.back_laser.ranges[0:int(average_separation - 1)])
        # #225-269
        # l2_left_data = np.array(self.back_laser.ranges[int(average_separation):int(average_separation*2)])
        # #270 - 314
        # l1_right_data = np.array(self.front_laser.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
        # #315 - 359
        # l1_front_right_data = np.array(self.front_laser.ranges[int(total_range - average_separation):int(total_range - 1)])

        l1_right_data = np.array(self.front_laser.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
        l1_front_right_data = np.array(self.front_laser.ranges[int(total_range - average_separation):int(total_range )])
        l2_right_data = np.array(self.back_laser.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
        l2_front_right_data = np.array(self.back_laser.ranges[int(total_range - average_separation):int(total_range)])
        l2_front_left_data = np.array(self.back_laser.ranges[0:int(average_separation)])
        l2_left_data = np.array(self.back_laser.ranges[int(average_separation):int(average_separation*2)])
        l1_front_left_data = np.array(self.front_laser.ranges[0:int(average_separation)])
        l1_left_data = np.array(self.front_laser.ranges[int(average_separation):int(average_separation*2)])
        

        # l1_front_left_data = np.array(self.front_laser.ranges[0:224])
        # l1_left_data = np.array(self.front_laser.ranges[225:450])

        # l2_right_data = np.array(self.back_laser.ranges[1350:1575])
        # l2_front_right_data = np.array(self.back_laser.ranges[1576:1799])
        # l2_front_left_data = np.array(self.back_laser.ranges[0:224])
        # l2_left_data = np.array(self.back_laser.ranges[225:450])

        # l1_right_data = np.array(self.front_laser.ranges[1350:1575])
        # l1_front_right_data = np.array(self.front_laser.ranges[1576:1799])      


        self.combined_laser = copy.copy(self.back_laser)
        self.combined_laser.ranges = []
        self.combined_laser.ranges.extend(list(l1_front_left_data))
        self.combined_laser.ranges.extend(list(l1_left_data))
        self.combined_laser.ranges.extend(list(l2_right_data))
        self.combined_laser.ranges.extend(list(l2_front_right_data))
        self.combined_laser.ranges.extend(list(l2_front_left_data))
        self.combined_laser.ranges.extend(list(l2_left_data))
        self.combined_laser.ranges.extend(list(l1_right_data))
        self.combined_laser.ranges.extend(list(l1_front_right_data))
        self.combained_laser_publisher.publish(self.combined_laser)
        print(len(self.combined_laser.ranges))
        
    def front_lidar_callback(self, scan_data):
         if not isinstance(scan_data, LaserScan): return
         new_laser = LaserScan()
         
         total_range = len(scan_data.ranges)
         average_separation = total_range / 8
         
         l1_right_data = np.array(scan_data.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
         l1_front_right_data = np.array(scan_data.ranges[int(total_range - average_separation):int(total_range)])
         l1_front_left_data = np.array(scan_data.ranges[0:int(average_separation)])
         l1_left_data = np.array(scan_data.ranges[int(average_separation):int(average_separation*2)])
         
         new_laser = copy.copy(scan_data)
         new_laser.ranges = []
         new_laser.ranges.extend(list(l1_right_data))
         new_laser.ranges.extend(list(l1_front_right_data))
         new_laser.ranges.extend(list(l1_front_left_data))
         new_laser.ranges.extend(list(l1_left_data))
         self.front_laser = copy.copy(scan_data)
         self.front_laser_publisher.publish(new_laser)
    
    def back_lidar_callback(self, scan_data):
         if not isinstance(scan_data, LaserScan): return
         new_laser = LaserScan()
         total_range = len(scan_data.ranges)
         average_separation = total_range / 8
         
         l2_right_data = np.array(scan_data.ranges[int(total_range - average_separation*2):int(total_range - average_separation)])
         l2_front_right_data = np.array(scan_data.ranges[int(total_range - average_separation):int(total_range)])
         l2_front_left_data = np.array(scan_data.ranges[0:int(average_separation)])
         l2_left_data = np.array(scan_data.ranges[int(average_separation):int(average_separation*2)])
         
         new_laser = copy.copy(scan_data)
         new_laser.ranges = []
         new_laser.ranges.extend(list(l2_right_data))
         new_laser.ranges.extend(list(l2_front_right_data))
         new_laser.ranges.extend(list(l2_front_left_data))
         new_laser.ranges.extend(list(l2_left_data))
         self.back_laser = copy.copy(scan_data)
         self.back_laser_publisher.publish(new_laser)

def main(args=None):
    rclpy.init(args=args)
    lidar_scan_node = LidarScanCustomNode()
    rclpy.spin(lidar_scan_node)
    lidar_scan_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
