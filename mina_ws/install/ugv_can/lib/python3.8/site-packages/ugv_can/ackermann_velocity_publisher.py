import can
import logging
import rclpy
from rclpy.node import Node
import math
from ackermann_interfaces.msg import AckermannFeedback


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
        self.angular= 0.0
        self.ackPublisher = self.create_publisher(AckermannFeedback,"feedback",50)
        self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_calback,
            10
        )

    def cmd_calback(self, msg):
        self.angular = msg.angular.z



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
            self.left_rpm  = ((value1 << 8) + value2) / 29.4 
            self.left_linear_speed = (2 * 3.14159 * WHEEL_RADIUS * self.left_rpm ) / 60



			
        if can_msg.arbitration_id == 0x200:
            hex_value3 = hex(can_msg.data[2])
            hex_value4 = hex(can_msg.data[3])

            value3 = self.twos_complement(hex_value3, 8)
            value4 = self.twos_complement(hex_value4, 8)
            self.right_rpm  = ((value3 << 8) + value4) / 29.4 
            self.right_linear_speed = (2 * 3.14159 * WHEEL_RADIUS * self.right_rpm ) / 60

               

        # self.ackPublisher.publish(self.right_linear_speed)
        vth = (self.right_linear_speed - self.left_linear_speed) / wheelbase * self.angular
        print(self.left_linear_speed, self.right_linear_speed, vth)
        vel_msg = AckermannFeedback()
        vel_msg.left_wheel_speed = self.left_linear_speed
        vel_msg.right_wheel_speed = self.right_linear_speed
        vel_msg.steering_angle = vth
        self.ackPublisher.publish(vel_msg)







def main(args=None):
	rclpy.init(args=args)

	can_subscriber = PCANBus()

	rclpy.spin(can_subscriber)

	can_subscriber.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
