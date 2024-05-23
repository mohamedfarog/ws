import os
from pathlib import Path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from ament_index_python.packages import get_package_share_directory, get_package_share_path

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

print("---------------------FRONT LIDAR LAUNCH---------------------")
def generate_launch_description():
    project_package_name = "mina_ugv"
    rplidar_config_path = Path(get_package_share_directory(project_package_name), 'config/rplidar_config.yaml')

    channel_type =  LaunchConfiguration('channel_type', default='serial')
    serial_port = LaunchConfiguration('serial_port', default='/dev/ttyUSB1')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='1000000')
    frame_id = LaunchConfiguration('frame_id', default='laser_front_link')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Standard')
    topic_name = LaunchConfiguration('topic_name', default='front_lidar')
    
    rplidar_node1 = Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='front_lidar',
            parameters=[
                # {'channel_type':channel_type,
                #          'serial_port': serial_port,
                #          'serial_baudrate': serial_baudrate,
                #          'frame_id': frame_id,
                #          'inverted': inverted,
                #          'angle_compensate': angle_compensate,
                #          'scan_mode': scan_mode,
                #          'topic_name': topic_name
                #          }
                rplidar_config_path
            ],
            output='screen')

    lidar1 = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output='screen',
            arguments=['1.15', '0', '0', '1.5', '0', '0', 'base_link', 'laser_front_link'],
        ) 
    return LaunchDescription([
        rplidar_node1,
        # lidar1
    ])
