import can
import logging
import rclpy
from rclpy.node import Node
import math

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Imu,MagneticField, JointState
from rclpy.clock import Clock
import random

WHEEL_RADIUS = 0.1 


# Constants
wheelbase = 0.35  # Distance between front and rear axles
track_width = 0.28  # Distance between the left and right wheels
max_steering_angle = math.radians(30)  # Maximum steering angle in radians

class PCANBus(Node):
    def __init__(self):
        super().__init__('mini_rover_driver')

        self.bus = can.interface.Bus(channel='can0', interface='socketcan', bitrate=500000)
        self.buffer = can.BufferedReader()
        self.notifier = can.Notifier(self.bus, [self.msg_rx_routine])
        self.left_rpm = 0.0
        self.right_rpm = 0.0
        self.left_linear_speed = 0.0
        self.right_linear_speed = 0.0
        self.WHEEL_BASE = 0.35
        self.velPublisher = self.create_publisher(Twist,"vel_raw",50)
        # self.statePublisher = self.create_publisher(JointState,"joint_states",10)


        

    def twos_complement(self, hex_string,  num_bits):
            value = int(hex_string, 16)
            if value & (1 << (num_bits - 1)):
                value -= 1 << num_bits
            return value
    
    def msg_rx_routine(self,can_msg):

        if can_msg.arbitration_id == 0x300:
            hex_value1 = hex(can_msg.data[2])
            hex_value2 = hex(can_msg.data[3])
            value1 = self.twos_complement(hex_value1, 8)
            value2 = self.twos_complement(hex_value2, 8)
            concatenated_hex = hex_value1[2:] + hex_value2[2:]
            self.left_rpm  = ((value1 << 8) + value2) / 29.4 
            velocity_m_per_min = self.linear_velocity_from_rpm(WHEEL_RADIUS, self.left_rpm)
            self.left_linear_speed = velocity_m_per_min / 60
			
        if can_msg.arbitration_id == 0x200:
            hex_value3 = hex(can_msg.data[2])
            hex_value4 = hex(can_msg.data[3])
            value3 = self.twos_complement(hex_value3, 8)
            value4 = self.twos_complement(hex_value4, 8)
            concatenated_hex = hex_value3[2:] + hex_value4[2:]
            self.right_rpm  = ((value3 << 8) + value4) / 29.4 
            velocity_m_per_min_right = self.linear_velocity_from_rpm(WHEEL_RADIUS, self.right_rpm)
            self.right_linear_speed = velocity_m_per_min_right / 60

        print("Left ", self.left_rpm,"Right ", self.right_rpm)
        time_stamp = Clock().now()
        state = JointState()
        state.header.stamp = time_stamp.to_msg()
        state.header.frame_id = "joint_states"
        state.name = ["rear_right_wheel_joint", "rear_left_wheel_joint","front_right_steer_joint","front_left_steer_joint",
                                "front_right_wheel_joint", "front_left_wheel_joint"]

        combined_speed = (self.left_linear_speed + self.right_linear_speed) / 2
        twist = Twist()
        vx = combined_speed
        vy = 0.0

        angular = (self.right_linear_speed - self.left_linear_speed) / track_width
        twist.linear.x = vx    #velocity in axis 
        twist.linear.y = vy   #steer angle
        twist.angular.z = angular   #this is invalued
        self.velPublisher.publish(twist)
        print("Linear velocity", combined_speed, "Angular ",angular)
        print(angular)

    def linear_velocity_from_rpm(self, radius, rpm):
        # Calculate linear velocity from wheel radius and RPM
        return 2 * math.pi * radius * rpm


def main(args=None):
    rclpy.init(args=args)

    can_subscriber = PCANBus()

    rclpy.spin(can_subscriber)

    can_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
