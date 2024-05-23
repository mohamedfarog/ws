import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Pose, Quaternion, Point, TransformStamped
from nav_msgs.msg import Odometry
import math
from rclpy.clock import Clock
from tf2_ros import TransformBroadcaster

class OdomPublisher(Node):
    def __init__(self):
        super().__init__('odom_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
        self.timer_ = self.create_timer(0.1, self.publish_odom)
        self.tf_broadcaster_ = TransformBroadcaster(self)
        self.last_time = Clock().now()
        
        # Initialize state
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Initialize odometry message
        self.odom = Odometry()
        self.odom.header.frame_id = 'odom'
        self.odom.child_frame_id = 'base_footprint'

        self.publish_tf = True

        self.pose_x = 0.0
        self.pose_y = 0.0
        self.pose_theta = 0.0
        self.wheelbase = 0.35  # Example value, adjust based on your robot's configuration
        self.linear_velocity = 0.0  # Initial linear velocity in m/s
        self.steering_angle = 0.5  # Initial steering angle in radians
        
        # Subscribe to the '/odom' topic to receive linear velocity updates
        self.subscription = self.create_subscription(
            Twist,
            'vel_raw',
            self.vel_callback,
            10
        )
        self.subscription  # prevent unused variable warning

        self.cmd_vel_subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.cmd_vel_subscription  # prevent unused variable warning

    def cmd_vel_callback(self, msg):
        # self.steering_angle = msg.angular.z
        pass
        
    def vel_callback(self, msg):
        self.linear_velocity = msg.linear.x
        self.steering_angle = msg.angular.z

    def publish_odom(self):
        current_time = Clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Compute odometry
        # Example: Replace with actual calculation based on Ackermann drive model
        # For example, you can use the velocity commands to integrate and estimate pose
        vx = self.linear_velocity  # Example value
        vy = 0.0001  # Example value
        vth = self.steering_angle  # Example value

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
            transform.child_frame_id = 'base_footprint'
            transform.transform.translation.x = self.x
            transform.transform.translation.y = self.y
            transform.transform.translation.z = 0.0
            transform.transform.rotation = quaternion
            self.tf_broadcaster_.sendTransform(transform)

        
def main(args=None):
    rclpy.init(args=args)

    odom_publisher = OdomPublisher()

    rclpy.spin(odom_publisher)

    odom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
