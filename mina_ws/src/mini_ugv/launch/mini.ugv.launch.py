from ament_index_python.packages import get_package_share_path
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    urdf_tutorial_path = get_package_share_path('mini_ugv')
    
    file_name = "navrover.urdf"
    default_model_path = urdf_tutorial_path / 'urdf/navrover.urdf'
    default_rviz_config_path = urdf_tutorial_path / 'rviz/accessories.rviz'

    gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
                                      description='Absolute path to robot urdf file')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    # Depending on gui parameter, either launch joint_state_publisher or joint_state_publisher_gui
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui'))
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )
    
    lidar_parameter_file = LaunchConfiguration('params_file')
    pkg_share = FindPackageShare(package='mini_ugv').find('mini_ugv')
    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               pkg_share, 'params', 'ydlidar.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')

    lidar_driver_node = Node(package='ydlidar_ros2_driver',
                            executable='ydlidar_ros2_driver_node',
                            name='ydlidar_ros2_driver_node',
                            output='screen',
                            emulate_tty=True,
                            parameters=[lidar_parameter_file],
                            )
    
    imu_node = Node(package='ugv_can',
                executable='imu_mad',
                name='imu_node',
                )
   
    joy_node = Node(
                package='joy',
                executable='joy_node',
                name='joy_node',
                output='screen',
            )

    joy_node_rover = Node(
                package='ugv_can',
                executable='ps_node',
                name='joy_node_rover',
                output='screen',
            )
    
    can_publisher_to_stm = Node(
            package='ugv_can',                 
            executable='sender',
            name='can_publisher',
            output='screen',
        )

    return LaunchDescription([
        gui_arg,
        model_arg,
        rviz_arg,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,

        params_declare,
        lidar_driver_node,
        # imu_node,

        joy_node,
        # joy_node_rover,

        can_publisher_to_stm

    ])
