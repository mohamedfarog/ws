
#Launch file 
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

    urdf_file_name = 'navrover.urdf'

    pkg_share = FindPackageShare(package='mini_ugv').find('mini_ugv')
    rviz_config_file = os.path.join(pkg_share, 'config','ydlidar.rviz')
    parameter_file = LaunchConfiguration('params_file')
    node_name = 'ydlidar_ros2_driver_node'

    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               pkg_share, 'params', 'ydlidar.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')

    lidar_driver_node = Node(package='ydlidar_ros2_driver',
                                executable='ydlidar_ros2_driver_node',
                                name='ydlidar_ros2_driver_node',
                                output='screen',
                                emulate_tty=True,
                                parameters=[parameter_file],
                                #node_namespace='/',
                                )

    imu_node = Node(package='ugv_can',
                    executable='imu_mad',
                    name='imu_mad',
                    # arguments=['-d', rviz_config_file],
                    )
    
    urdf_path = os.path.join(
        get_package_share_directory('mini_ugv'),
        'urdf',
        urdf_file_name)

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()
        
	#Launch file 
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_desc
            }],
        ),
        
        Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
            ),
        Node(
            package='ugv_can',                   #CAN PUBLISHER
            executable='sender',
            name='can_publisher',
            output='screen',
        ),
        Node(
            package='ugv_can',                   #CAN PUBLISHER
            executable='first_odom_publisher',
            name='odom_publisher',
            output='screen',
        ),
        Node(
            package='ugv_can',                   #CAN PUBLISHER
            executable='first_odom_while_pub',
            name='odom_while_pub',
            output='screen',
        ),
        
#########################################  JOY STICK  ######################

        # Node(
        #     package='joy',
        #     executable='joy_node',
        #     name='joy_node',
        #     output='screen',
        # ),

        # Node(
        #     package='ugv_can',
        #     executable='ps_node',
        #     name='joy_node_rover',
        #     output='screen',
        # ),

###############################################################################
        params_declare,
        
        lidar_driver_node,
        imu_node,
    ])

