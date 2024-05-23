import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Quaternion, TransformStamped, Vector3
from nav_msgs.msg import Odometry
import math

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.odom_publisher = self.create_publisher(Odometry, 'odom', 10)
        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'vel_raw',
            self.cmd_vel_callback,
            10)
        self.current_time = self.get_clock().now()
        self.last_time = self.get_clock().now()

        # Parameters for odometry calculation
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.vx = 0.0
        self.vtheta = 0.0
        self.wheelbase = 0.5  # Replace with the actual wheelbase of your robot

    def cmd_vel_callback(self, msg):
        self.current_time = self.get_clock().now()

        dt = (self.current_time - self.last_time).nanoseconds / 1e9

        linear_speed = msg.linear.x
        angular_speed = msg.angular.z

        self.vx = linear_speed
        self.vtheta = angular_speed

        delta_x = (self.vx * math.cos(self.theta)) * dt
        delta_y = (self.vx * math.sin(self.theta)) * dt
        delta_theta = self.vtheta * dt

        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

        odom_msg = Odometry()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_footprint'
        odom_msg.header.stamp = self.current_time.to_msg()
        odom_msg.pose.pose.position.x = self.x
        odom_msg.pose.pose.position.y = self.y
        odom_msg.pose.pose.position.z = 0.0
        odom_msg.pose.pose.orientation = self.quaternion_from_euler(0, 0, self.theta)
        odom_msg.twist.twist.linear.x = self.vx
        odom_msg.twist.twist.angular.z = self.vtheta

        self.odom_publisher.publish(odom_msg)

        self.last_time = self.current_time

    def quaternion_from_euler(self, roll, pitch, yaw):
        q = Quaternion()
        q.x = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        q.y = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
        q.z = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
        q.w = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
        return q

def main(args=None):
    rclpy.init(args=args)
    odometry_publisher = OdometryPublisher()
    rclpy.spin(odometry_publisher)
    odometry_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
