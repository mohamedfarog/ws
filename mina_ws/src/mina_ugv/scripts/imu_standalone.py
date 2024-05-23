#!/usr/bin/env python3
import time
import math
import serial
import struct
import numpy as np
import threading
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu,MagneticField

key = 0
flag = 0
buff = {}
angularVelocity = [0, 0, 0]
acceleration = [0, 0, 0]
magnetometer = [0, 0, 0]
angle_degree = [0, 0, 0]

def hex_to_short(raw_data):
	return list(struct.unpack("hhhh", bytearray(raw_data)))


def check_sum(list_data, check_data):
	return sum(list_data) & 0xff == check_data


def handle_serial_data(raw_data):
	global buff, key, angle_degree, magnetometer, acceleration, angularVelocity, pub_flag
	angle_flag = False
	buff[key] = raw_data

	key += 1
	if buff[0] != 0x55:
		key = 0
		return
	# According to the judgment of the data length bit, the corresponding length data can be obtained
	if key < 11:
		return
	else:
		data_buff = list(buff.values())  # Get dictionary ownership value
		if buff[1] == 0x51:
			if check_sum(data_buff[0:10], data_buff[10]):
				acceleration = [hex_to_short(data_buff[2:10])[i] / 32768.0 * 16 * 9.8 for i in range(0, 3)]
			else:
				print('0x51 Check failure')

		elif buff[1] == 0x52:
			if check_sum(data_buff[0:10], data_buff[10]):
				angularVelocity = [hex_to_short(data_buff[2:10])[i] / 32768.0 * 2000 * math.pi / 180 for i in
								   range(0, 3)]
			else:
				print('0x52 Check failure')

		elif buff[1] == 0x53:
			if check_sum(data_buff[0:10], data_buff[10]):
				angle_degree = [hex_to_short(data_buff[2:10])[i] / 32768.0 * 180 for i in range(0, 3)]
				angle_flag = True
			else:
				print('0x53 Check failure')
		elif buff[1] == 0x54:
			if check_sum(data_buff[0:10], data_buff[10]):
				magnetometer = hex_to_short(data_buff[2:10])
			else:
				print('0x54 Check failure')
		else:
			buff = {}
			key = 0

		buff = {}
		key = 0
		return angle_flag

def get_quaternion_from_euler(roll, pitch, yaw):
	"""
	Convert an Euler angle to a quaternion.

	Input
	  :param roll: The roll (rotation around x-axis) angle in radians.
	  :param pitch: The pitch (rotation around y-axis) angle in radians.
	  :param yaw: The yaw (rotation around z-axis) angle in radians.

	Output
	  :return qx, qy, qz, qw: The orientation in quaternion [x,y,z,w] format
	"""
	qx = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(
		yaw / 2)
	qy = np.cos(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.cos(pitch / 2) * np.sin(
		yaw / 2)
	qz = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(
		yaw / 2)
	qw = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(
		yaw / 2)

	return [qx, qy, qz, qw]


class IMUDriverNode(Node):
	def __init__(self, port_name):
		super().__init__('IMUDriverNode')

		self.imu_msg = Imu()
		self.imu_msg.header.frame_id = 'imu_link'

		self.mag_msg = MagneticField()
		self.mag_msg.header.frame_id = 'imu_link'

		self.declare_parameter("serial_port","/dev/imu_usb")
		self.serial_port = self.get_parameter('serial_port').get_parameter_value().string_value

		self.declare_parameter("baudrate",9600)
		self.baudrate = self.get_parameter('baudrate').get_parameter_value().integer_value

		self.declare_parameter("imu_topic","imu/og_data_raw")
		self.imu_topic = self.get_parameter('imu_topic').get_parameter_value().string_value

		self.declare_parameter("mag_topic","imu/og_mag")
		self.mag_topic = self.get_parameter('mag_topic').get_parameter_value().string_value
		
		self.imu_pub = self.create_publisher(Imu, self.imu_topic, 10)
		self.mag_pub = self.create_publisher(MagneticField, self.mag_topic, 10)
		self.driver_thread = threading.Thread(target=self.driver_loop, args=(port_name,))
		self.driver_thread.start()

	def driver_loop(self, port_name):
	   
		try:
			wt_imu = serial.Serial(port=self.serial_port, baudrate=self.baudrate, timeout=0.5)
			if wt_imu.isOpen():
				self.get_logger().info("\033[32mSerial port opened successfully...\033[0m")
			else:
				wt_imu.open()
				self.get_logger().info("\033[32mSerial port opened successfully...\033[0m")
		except Exception as e:
			print(e)
			self.get_logger().info("\033[31mSerial port opening failure\033[0m")
			exit(0)

		while True:
		
			try:
				buff_count = wt_imu.inWaiting()
			except Exception as e:
				print("exception:" + str(e))
				print("imu disconnect")
				exit(0)
			else:
				if buff_count > 0:
					buff_data = wt_imu.read(buff_count)
					for i in range(0, buff_count):
						tag = handle_serial_data(buff_data[i])
						if tag:
							self.imu_data()
							self.mag_data()

	def imu_data(self):
		accel_x, accel_y, accel_z = acceleration[0], acceleration[1], acceleration[2]  # struct.unpack('hhh', accel_raw)
		accel_scale = 16 / 32768.0
		accel_x, accel_y, accel_z = accel_x * accel_scale, accel_y * accel_scale, accel_z * accel_scale

		gyro_x, gyro_y, gyro_z = angularVelocity[0], angularVelocity[1], angularVelocity[2]  # struct.unpack('hhh', gyro_raw)
		gyro_scale = 2000 / 32768.0
		gyro_x, gyro_y, gyro_z = math.radians(gyro_x * gyro_scale), math.radians(gyro_y * gyro_scale), math.radians(gyro_z * gyro_scale)

		dt = 0.01
		wx, wy, wz = gyro_x, gyro_y, gyro_z
		ax, ay, az = accel_x, accel_y, accel_z
		roll, pitch, yaw = self.compute_orientation(wx, wy, wz, ax, ay, az, dt)

		self.imu_msg.header.stamp = self.get_clock().now().to_msg()
		self.imu_msg.linear_acceleration.x = accel_x 
		self.imu_msg.linear_acceleration.y = accel_y 
		self.imu_msg.linear_acceleration.z = accel_z
		self.imu_msg.angular_velocity.x = gyro_x
		self.imu_msg.angular_velocity.y = gyro_y
		self.imu_msg.angular_velocity.z = gyro_z

		angle_radian = [angle_degree[i] * math.pi / 180 for i in range(3)]

		qua = get_quaternion_from_euler(angle_radian[0], angle_radian[1], angle_radian[2])

		self.imu_msg.orientation.x = qua[0]
		self.imu_msg.orientation.y = qua[1]
		self.imu_msg.orientation.z = qua[2]
		self.imu_msg.orientation.w = qua[3]

		self.imu_pub.publish(self.imu_msg)

	def mag_data(self):
		mag_x, mag_y, mag_z = magnetometer[0], magnetometer[1], magnetometer[2]  # struct.unpack('hhh', accel_raw)
		accel_scale = 1.0
		mag_x, mag_y, mag_z = mag_x * accel_scale, mag_y * accel_scale, mag_z * accel_scale

		
		self.imu_msg.header.stamp = self.get_clock().now().to_msg()
		self.mag_msg.magnetic_field.x = mag_x
		self.mag_msg.magnetic_field.y = mag_y
		self.mag_msg.magnetic_field.z = mag_z
		self.mag_pub.publish(self.mag_msg)

	def compute_orientation(self, wx, wy, wz, ax, ay, az, dt):
		Rx = np.array([[1, 0, 0],
					   [0, math.cos(ax), -math.sin(ax)],
					   [0, math.sin(ax), math.cos(ax)]])
		Ry = np.array([[math.cos(ay), 0, math.sin(ay)],
					   [0, 1, 0],
					   [-math.sin(ay), 0, math.cos(ay)]])
		Rz = np.array([[math.cos(wz), -math.sin(wz), 0],
					   [math.sin(wz), math.cos(wz), 0],
					   [0, 0, 1]])
		R = Rz.dot(Ry).dot(Rx)

		roll = math.atan2(R[2][1], R[2][2])
		pitch = math.atan2(-R[2][0], math.sqrt(R[2][1] ** 2 + R[2][2] ** 2))
		yaw = math.atan2(R[1][0], R[0][0])

		return roll, pitch, yaw


def main():
	rclpy.init()
	node = IMUDriverNode('/dev/ttyUSB2')

	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()