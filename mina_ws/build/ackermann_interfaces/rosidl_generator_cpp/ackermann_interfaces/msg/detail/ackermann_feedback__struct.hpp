// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice

#ifndef ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_HPP_
#define ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ackermann_interfaces__msg__AckermannFeedback __attribute__((deprecated))
#else
# define DEPRECATED__ackermann_interfaces__msg__AckermannFeedback __declspec(deprecated)
#endif

namespace ackermann_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AckermannFeedback_
{
  using Type = AckermannFeedback_<ContainerAllocator>;

  explicit AckermannFeedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->steering_angle = 0.0f;
      this->left_wheel_speed = 0.0f;
      this->right_wheel_speed = 0.0f;
    }
  }

  explicit AckermannFeedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->steering_angle = 0.0f;
      this->left_wheel_speed = 0.0f;
      this->right_wheel_speed = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _steering_angle_type =
    float;
  _steering_angle_type steering_angle;
  using _left_wheel_speed_type =
    float;
  _left_wheel_speed_type left_wheel_speed;
  using _right_wheel_speed_type =
    float;
  _right_wheel_speed_type right_wheel_speed;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__steering_angle(
    const float & _arg)
  {
    this->steering_angle = _arg;
    return *this;
  }
  Type & set__left_wheel_speed(
    const float & _arg)
  {
    this->left_wheel_speed = _arg;
    return *this;
  }
  Type & set__right_wheel_speed(
    const float & _arg)
  {
    this->right_wheel_speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ackermann_interfaces__msg__AckermannFeedback
    std::shared_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ackermann_interfaces__msg__AckermannFeedback
    std::shared_ptr<ackermann_interfaces::msg::AckermannFeedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AckermannFeedback_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->steering_angle != other.steering_angle) {
      return false;
    }
    if (this->left_wheel_speed != other.left_wheel_speed) {
      return false;
    }
    if (this->right_wheel_speed != other.right_wheel_speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const AckermannFeedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AckermannFeedback_

// alias to use template instance with default allocator
using AckermannFeedback =
  ackermann_interfaces::msg::AckermannFeedback_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ackermann_interfaces

#endif  // ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_HPP_
