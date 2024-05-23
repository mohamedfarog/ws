#!/usr/bin/env python3

import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from math import pi

def generate_launch_description():

    pkg_share = FindPackageShare(package='mini_ugv').find('mini_ugv')

    robot_localization_file_path = os.path.join(pkg_share, 'config/ekf3.yaml') 
    ld = LaunchDescription()

    # imu_filter_config = os.path.join(get_package_share_directory('mini_ugv'), 'config/imu_filter_config.yaml')
    
    # imu_filter_madgwick = Node(
    # 	package='imu_filter_madgwick',
    #     executable='imu_filter_madgwick_node',
    #     parameters=[imu_filter_config],
    #     remappings=[('/imu/og_data_raw', '/imu/og_data_raw')],
    #     output='screen'
    #     ),
    
    start_robot_localization_cmd = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        remappings = [('/odometry/filtered', '/odom')],
        parameters=[robot_localization_file_path])
    
    # ld.add_action(imu_filter_madgwick)
    ld.add_action(start_robot_localization_cmd)

    return ld
