import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Twist, Point
from tf2_ros import TransformBroadcaster,TransformStamped
import math

class AckermannOdometryPublisher(Node):

    def __init__(self):
        super().__init__('ackermann_odometry_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.last_time = self.get_clock().now()

        # Parameters
        self.wheel_base = 0.3  # Example value, replace with actual value
        self.publish_tf = True

        # Initialize odometry message
        self.odom = Odometry()
        self.odom.header.frame_id = 'odom'
        self.odom.child_frame_id = 'base_link'

        # Initialize state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def timer_callback(self):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Compute odometry
        # Example: Replace with actual calculation based on Ackermann drive model
        # For example, you can use the velocity commands to integrate and estimate pose
        vx = 0.0  # Example value
        vy = 0.0  # Example value
        vth = 0.0  # Example value

        delta_x = vx * math.cos(self.theta) - vy * math.sin(self.theta)
        delta_y = vx * math.sin(self.theta) + vy * math.cos(self.theta)
        delta_th = vth

        self.x += delta_x * dt
        self.y += delta_y * dt
        self.theta += delta_th * dt

        # Publish odometry message
        quaternion = Quaternion()
        quaternion.x = 0.0
        quaternion.y = 0.0
        quaternion.z = math.sin(self.theta / 2)
        quaternion.w = math.cos(self.theta / 2)

        self.odom.header.stamp = current_time.to_msg()
        self.odom.pose.pose.position = Point(x=self.x, y=self.y, z=0.0)
        self.odom.pose.pose.orientation = quaternion

        # Twist
        self.odom.twist.twist.linear.x = vx
        self.odom.twist.twist.linear.y = vy
        self.odom.twist.twist.angular.z = vth

        # Publish odometry message
        self.publisher_.publish(self.odom)

        # Publish TF
        if self.publish_tf:
            transform = TransformStamped()
            transform.header.stamp = current_time.to_msg()
            transform.header.frame_id = 'odom'
            transform.child_frame_id = 'base_link'
            transform.transform.translation.x = self.x
            transform.transform.translation.y = self.ys
            transform.transform.translation.z = 0.0
            transform.transform.rotation = quaternion
            self.tf_broadcaster.sendTransform(transform)


def main(args=None):
    rclpy.init(args=args)
    odometry_publisher = AckermannOdometryPublisher()
    rclpy.spin(odometry_publisher)
    odometry_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
