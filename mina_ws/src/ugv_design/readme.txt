1. Display ugv in rviz

    ros2 launch ugv_deisgn display.launch.py

2. Mapping using ugv

    ros2 launch ugv_design ugv_design.launch.py  - spawning in gazebo

    ros2 launch ugv_design mapping.launch.py     - start rviz and robot state
                                                    publishers for mapping
    
    ros2 launch ugv_design online_async.launch.py - mapping parameters

    rqt for driving the robot

3. Starting the navigation stack'

    ros2 launch ugv_design ugv_design.launch.py   - Spawning the ugv in gazebo

    ros2 launch ugv_design navigation2.launch.py  - starting the navigation stack

