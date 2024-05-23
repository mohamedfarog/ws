import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare



def generate_launch_description():
    # TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

    urdf_file_name = 'navrover.xacro'

    pkg_share = FindPackageShare(package='mini_ugv').find('mini_ugv')
    rviz_config_file = os.path.join(pkg_share, 'config','ydlidar.rviz')
    parameter_file = LaunchConfiguration('params_file')
    node_name = 'ydlidar_ros2_driver_node'

    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               pkg_share, 'params', 'ydlidar.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')

    driver_node = Node(package='ydlidar_ros2_driver',
                                executable='ydlidar_ros2_driver_node',
                                name='ydlidar_ros2_driver_node',
                                output='screen',
                                emulate_tty=True,
                                parameters=[parameter_file],
                                #node_namespace='/',
                                )
    laser_tf = Node(package='tf2_ros',
                    executable='static_transform_publisher',
                    name='static_tf_pub_laser',
                    arguments=['0', '0', '1.7','0', '0', '0', '1','base_link','laser_frame']
                    )
    
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
    imu_node = Node(package='ugv_can',
                    executable='imu_mad',
                    name='imu_mad',
                    # arguments=['-d', rviz_config_file],
                    )
    



    robot_localization_file_path = os.path.join(pkg_share, 'config/ekf.yaml') 

    
    robot_loc =    Node(
            package='robot_localization',            #ROBOT LOCALIZATION
            executable='ekf_node',
            name='ekf_localization',
            output='screen',
            # remappings = [('/odometry/filtered','/odom')],
            parameters=[robot_localization_file_path]
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

        # Node(
        #     package='robot_localization',            #ROBOT LOCALIZATION
        #     executable='ekf_node',
        #     name='ekf_localization',
        #     output='screen',
        #     remappings = [('/odometry/filtered','/odom')],
        #     parameters=[robot_localization_file_path]
        # ),

        Node(
            package='ugv_can',                   #CAN PUBLISHER
            executable='sender',
            name='can_publisher',
            output='screen',
        ),

        # Node(
        #     package='ugv_can',                   #CAN RECEIVER
        #     executable='odom_publisher',
        #     name='can_publisher',
        #     output='screen',
        # ),

        # Node(
        #     package='ugv_can',                   #ODOM
        #     executable='odom_while_pub',
        #     name='can_publisher',
        #     output='screen',
        # ),

        # Node(
        #     package='ugv_can',                   #ODOM
        #     executable='odom_final',
        #     name='odom_final',
        #     output='screen',
        # ),

        # Node(
        #     package='ugv_can',                   #ODOM
        #     executable='imu_node',
        #     name='imu_node',
        #     output='screen',
        # ),

#########################################  JOY STICK  ######################

        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
        ),

        Node(
            package='ugv_can',
            executable='ps_node',
            name='joy_node_rover',
            output='screen',
        ),

###############################################################################
        
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
        params_declare,
        driver_node,
        laser_tf,
        # imu_tf,
        # rviz2_node,
        imu_node,
        # robot_loc
    ])

