#!/usr/bin/env python3
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    # Realsense Node
    realsense_configuration_path = Path(get_package_share_directory('mina_ugv'), 'config/realsense_config.yaml')
    
    front_camera_node = Node(
    	package='realsense2_camera',
        name="camera_front",
        executable='realsense2_camera_node',
        parameters=[
                   realsense_configuration_path
        ],
        output='screen'
        )
    ld.add_action(front_camera_node)

    back_camera_node = Node(
    	package='realsense2_camera',
        name="camera_back",
        executable='realsense2_camera_node',
        parameters=[
                   realsense_configuration_path
        ],
        output='screen'
        )    
    ld.add_action(back_camera_node)
    
    front_camera_tf = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output='screen',
            arguments=['0.1905', '0', '0.3302', '0', '0', '0', 'base_link', 'front_camera_link'],
        ) 
    # ld.add_action(front_camera_tf)

    back_camera_tf = Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output='screen',
            arguments=['-0.1905', '0', '0.3302', '3.14', '0', '0', 'base_link', 'back_camera_link'],
        ) 
    # ld.add_action(back_camera_tf)

    
    return ld

