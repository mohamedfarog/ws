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

print("------------------LIDAR LAUNCH---------------------")

def generate_launch_description():
    project_package_name = "mina_ugv"
    rplidar_config_path = Path(get_package_share_directory(project_package_name), 'config/rplidar_config.yaml')

    front_lidar_node = Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='front_lidar',
            parameters=[
                rplidar_config_path
            ],
            output='screen')
    
    back_lidar_node = Node(
            package='rplidar_ros',
            executable='rplidar_node',
            name='back_lidar',
            parameters=[
                rplidar_config_path
            ],
            output='screen')

    back_lidar_tf = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output='screen',
            arguments=['-1.15', '0', '0', '-1.57', '0', '0', 'base_link', 'laser_back_link'],
        )

    front_lidar_tf = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output='screen',
            arguments=['1.15', '0', '0', '1.5', '0', '0', 'base_link', 'laser_front_link'],
        )
     
    return LaunchDescription([
        front_lidar_node,
        back_lidar_node,
        # back_lidar_tf,
        # front_lidar_tf
    ])
