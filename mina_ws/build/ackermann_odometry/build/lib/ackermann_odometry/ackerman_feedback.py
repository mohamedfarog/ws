import rclpy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Header
from rclpy.clock import Clock

from ackermann_interfaces.msg import AckermannFeedback

import can
import math

WHEEL_RADIUS = 0.1 

class AckermannFeedBackNode(Node):
    """Publishes ackermann control by joystick"""

    def __init__(self):
        super().__init__('ackermann_teleop_joy')

        self.bus = can.interface.Bus(channel='can0', interface='socketcan', bitrate=500000)
        self.buffer = can.BufferedReader()
        self.notifier = can.Notifier(self.bus, [self.msg_rx_routine])

        self.left_rpm = 0.0
        self.right_rpm = 0.0
        self.left_linear_speed = 0.0
        self.right_linear_speed = 0.0
        self.WHEEL_BASE = 0.35

        self.create_subscription(
            AckermannDriveStamped,
            'ackermann_cmd',
            self.joy_callback,
            10
        )

        self.publisher = self.create_publisher(AckermannFeedback, 'feedback', 10)

    def joy_callback(self, msg: AckermannDriveStamped):
        # print(msg.drive.steering_angle)

        newfeed = AckermannFeedback()
        time_stamp = Clock().now()
        newfeed.header.stamp = time_stamp.to_msg()
        newfeed.steering_angle = msg.drive.steering_angle
        newfeed.left_wheel_speed = self.left_linear_speed
        newfeed.right_wheel_speed = self.right_linear_speed
        self.publisher.publish(newfeed)

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
            self.left_linear_speed = (2 * 3.14159 * WHEEL_RADIUS * self.left_rpm ) / 60
			# print("300")
               
            # Calculate linear velocity
            velocity_m_per_min = self.linear_velocity_from_rpm(WHEEL_RADIUS, self.left_rpm)
            # Convert linear velocity to meters per second
            self.left_linear_speed = velocity_m_per_min / 60


			
        if can_msg.arbitration_id == 0x200:
            hex_value3 = hex(can_msg.data[2])
            hex_value4 = hex(can_msg.data[3])

            value3 = self.twos_complement(hex_value3, 8)
            value4 = self.twos_complement(hex_value4, 8)
            concatenated_hex = hex_value3[2:] + hex_value4[2:]
                # decimal_sum = int(concatenated_hex, 16)
            self.right_rpm  = ((value3 << 8) + value4) / 29.4 
            # self.right_linear_speed = (2 * 3.14159 * WHEEL_RADIUS * self.right_rpm ) / 60
			# print("200")
               
            # Calculate linear velocity
            velocity_m_per_min_right = self.linear_velocity_from_rpm(WHEEL_RADIUS, self.right_rpm)
            # Convert linear velocity to meters per second
            self.right_linear_speed = velocity_m_per_min_right / 60

        
    def linear_velocity_from_rpm(self,radius, rpm):
        # Convert RPM to radians per minute
        omega = rpm * (2 * math.pi)
        # Calculate linear velocity
        velocity = radius * omega
        return velocity
    
    
    
def main(args=None):
    rclpy.init(args=args)

    ackermann_teleop_joy = AckermannFeedBackNode()

    rclpy.spin(ackermann_teleop_joy)

    ackermann_teleop_joy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
