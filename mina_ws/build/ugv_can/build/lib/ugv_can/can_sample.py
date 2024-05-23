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
        self.steering_angle = 0.0
        self.velPublisher = self.create_publisher(Twist,"vel_raw",50)
        self.statePublisher = self.create_publisher(JointState,"joint_states",10)
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )

        
    def cmd_vel_callback(self, msg):
        # Update steering angle based on the received Twist message
        self.steering_angle = msg.angular.z

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


        if self.left_rpm == 0 and self.right_rpm == 0 or self.steering_angle == 0:
            return

        print("Left ", self.left_rpm,"Right ", self.right_rpm)
        time_stamp = Clock().now()
        
        combined_speed = (self.left_linear_speed + self.right_linear_speed) / 2
        twist = Twist()
        vx = combined_speed
        vy = 1.0
        # print("Combined Speed ",combined_speed)
        # angular = (self.right_linear_speed - self.left_linear_speed) / self.WHEEL_BASE
        # steering_angle_temp = math.radians(30)  # 30 degrees converted to radians
        # angular = self.calculate_angular_velocity(combined_speed, self.WHEEL_BASE, steering_angle_temp)
        # angular = self.steering_angle
        # angular = math.radians(self.steering_angle)
        angular = self.angular_to_steering(self.steering_angle)

        # print(angular)

        twist.linear.x = vx    #velocity in axis 
        twist.linear.y = vy   #steer angle
        twist.angular.z = angular   #this is invalued
        self.velPublisher.publish(twist)

        # print("Angular velocity:", angular, "rad/s")
        # print("Linear velocity left:", self.left_linear_speed)
        # print("Linear velocity right:", self.right_linear_speed)
        # print("Linear velocity", combined_speed, "Angular ",angular)

        state = JointState()
        state.header.stamp = time_stamp.to_msg()
        state.header.frame_id = "joint_states"
        state.name = ["rear_right_wheel_joint", 
                      "rear_left_wheel_joint",
                      "front_right_steer_joint",
                      "front_left_steer_joint",
                      "front_right_wheel_joint", 
                      "front_left_wheel_joint"]
        
        # #turn to radis
        steer_radis = angular*3.1416/180.0
        # state.position = [0.0, 0.0, 0.0, 0.0,0.0, 0.0]
        if not vx == angular == 0:
            # i = 0.0
            temp_angular = angular * 0.3
            state.position = [self.right_linear_speed, self.left_linear_speed, temp_angular,temp_angular,self.right_linear_speed, self.left_linear_speed]
            # state.velocity = [self.right_linear_speed, self.left_linear_speed, temp_angular,temp_angular,self.right_linear_speed, self.left_linear_speed]
            # i = random.uniform(-3.14, 3.14)
            # state.position = [i, i, angular, angular, i, i]
            # state.position = [i, i, steer_radis, steer_radis, i, i]

        self.statePublisher.publish(state)	

    def calculate_angular_velocity(self,v, L, theta):
        R = L / math.tan(theta)
        return v / R	
    
    def linear_velocity_from_rpm(self,radius, rpm):
        # Convert RPM to radians per minute
        omega = rpm * (2 * math.pi)
        # Calculate linear velocity
        velocity = radius * omega
        return velocity
    

    def angular_to_steering(self,angular_z):
        if angular_z == 0:
            return 0.0  # No steering angle if angular velocity is zero
        
        turning_radius = wheelbase / math.tan(angular_z)

        # Calculate steering angle for inner and outer wheels
        inner_steering_angle = math.atan(wheelbase / (turning_radius - track_width / 2))
        outer_steering_angle = math.atan(wheelbase / (turning_radius + track_width / 2))

        # Choose the maximum steering angle between the two wheels
        steering_angle = max(min(inner_steering_angle, max_steering_angle), -max_steering_angle)

        return float(steering_angle)


def main(args=None):
	rclpy.init(args=args)

	can_subscriber = PCANBus()

	rclpy.spin(can_subscriber)

	can_subscriber.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
