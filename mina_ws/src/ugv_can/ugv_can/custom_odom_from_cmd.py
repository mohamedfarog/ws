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
        # self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.subscription = self.create_subscription(Twist, 'vel_raw', self.listener_callback, 10)
        
        self.pose_x = 0.0
        self.pose_y = 0.0
        self.pose_theta = 0.0
        self.wheelbase = 0.35  # Example value, adjust based on your robot's configuration
        self.steer_ratio = 0.5  # Example value, adjust based on your robot's configuration
        self.linear_velocity = 0.0  # Linear velocity in m/s
        self.steering_angle = 0.0  # Initial steering angle in radians
        self.last_time = Clock().now()

    def listener_callback(self,msg):
            self.linear_velocity = msg.linear.x
            # if msg.linear.x != 0:
            self.steering_angle = msg.angular.z
            

    def publish_odom(self):
        odom_msg = Odometry()

        current_time = Clock().now()
        odom_msg.header.stamp = current_time.to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_footprint'

        # Update the robot's pose based on Ackermann steering odometry equations
        delta_time = 0.1

        vx = self.linear_velocity # Example value
        vy = 0.0  # Example value
        vth = self.steering_angle  # Example value
        
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time
        
        # if vx > 0 and vx < 0 or vth > 0 and vth < 0:
        #      return

        # delta_distance = self.linear_velocity * delta_time
        # delta_theta = (delta_distance / self.wheelbase) * math.tan(self.steering_angle)

        # self.pose_x += delta_distance * math.cos(self.pose_theta + delta_theta / 2)
        # self.pose_y += delta_distance * math.sin(self.pose_theta + delta_theta / 2)
        # self.pose_theta += delta_theta


        delta_x = vx * math.cos(self.pose_theta) - vy * math.sin(self.pose_theta)
        delta_y = vx * math.sin(self.pose_theta) + vy * math.cos(self.pose_theta)
        delta_th = vth

        self.pose_x += delta_x * dt
        self.pose_y += delta_y * dt
        self.pose_theta += delta_th * dt


        # Populate the odometry message
        # odom_msg.pose.pose.position = Point(x=self.pose_x, y=self.pose_y, z=0.0)
        # odom_msg.pose.pose.orientation = self.get_quaternion(self.pose_theta)
        odom_msg.twist.twist.linear.x = self.linear_velocity
        odom_msg.twist.twist.angular.z = (self.linear_velocity / self.wheelbase) * math.tan(self.steering_angle)
        # print("Print odom ")
        print("pose x :", self.pose_x , "Posee y: ",self.pose_y, "Pose theta:",self.pose_theta)
        self.publisher_.publish(odom_msg)

        t = TransformStamped()
        t.header.stamp = current_time.to_msg()
        t.header.frame_id = "odom"
        t.child_frame_id = "base_footprint"
        t.transform.translation.x = self.pose_x
        t.transform.translation.y = self.pose_y
        t.transform.translation.z = 0.0
        
        t.transform.rotation = self.get_quaternion(self.pose_theta)
        
        self.tf_broadcaster_.sendTransform(t)
        

    def get_quaternion(self, theta):
        return Quaternion(
            x=0.0,
            y=0.0,
            z=math.sin(theta / 2.0),
            w=math.cos(theta / 2.0)
        )

def main(args=None):
    rclpy.init(args=args)

    odom_publisher = OdomPublisher()

    rclpy.spin(odom_publisher)

    odom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
