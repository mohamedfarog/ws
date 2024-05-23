import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

    urdf_file_name = 'navrover.urdf'

    share_dir = get_package_share_directory('mini_ugv')
    rviz_config_file = os.path.join(share_dir, 'config','ydlidar.rviz')

    # laser_tf = Node(package='tf2_ros',
    #                 executable='static_transform_publisher',
    #                 name='static_tf_pub_laser',
    #                 arguments=['0', '0', '1.7','0', '0', '0', '1','base_link','laser_frame']
                    # )
    
    # imu_tf = Node(package='tf2_ros',
    #                 executable='static_transform_publisher',
    #                 name='static_tf_pub_laser',
    #                 arguments=['-0.7', '0', '1.7','0', '0', '0', '1','base_link','imu_link']
                    # )
    rviz2_node = Node(package='rviz2',
                    executable='rviz2',
                    name='rviz2',
                    arguments=['-d', rviz_config_file],
                    )
    
    

    # print('urdf_file_name : {}'.format(urdf_file_name))

    urdf_path = os.path.join(
        get_package_share_directory('mini_ugv'),
        'urdf',
        urdf_file_name)

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    

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
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                name="joint_state_publisher_gui",
            ),
        
        # Node(
        #     package='imu_ros',
        #     executable='odom',
        #     name='odom_pub',
        #     output='screen',
        # ),
        
        # Node(
        #     package='imu_ros',
        #     executable='imu_pub',
        #     name='imu_pub',
        #     output='screen',          
        # ),
        
        # Node(
        # package='joint_state_publisher_gui',
        # executable='joint_state_publisher_gui',
        # ),
        # laser_tf,
        # imu_tf,
        rviz2_node,
    ])

