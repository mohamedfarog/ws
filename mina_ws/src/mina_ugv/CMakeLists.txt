cmake_minimum_required(VERSION 3.8)
project(mina_ugv)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(turtlesim REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(laser_geometry REQUIRED)


#==CPP===============================================================#
# Include Cpp "include" directory
include_directories(include)

add_executable(odom_publisher_ackermann_node src/Odom_Publisher.cpp)
ament_target_dependencies(odom_publisher_ackermann_node rclcpp tf2 tf2_ros nav_msgs turtlesim geometry_msgs)

# Install Cpp executables
install(TARGETS
  odom_publisher_ackermann_node
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch meshes rviz urdf worlds config params maps models
  DESTINATION share/${PROJECT_NAME}
)

#==PYTHONS===============================================================#
# Install Python modules
ament_python_install_package(${PROJECT_NAME})

install(DIRECTORY
  scripts/modules
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python executables
install(PROGRAMS
  scripts/ugv_driver.py
  scripts/navrover_ps4_ctrl.py
  scripts/lidar_avoidance.py
  scripts/lidar_scan_multiple.py
  scripts/lidar_to_point_publish.py
  scripts/publish_gps_data.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
