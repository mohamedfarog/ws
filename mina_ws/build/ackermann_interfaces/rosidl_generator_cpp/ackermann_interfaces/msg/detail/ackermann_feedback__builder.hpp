// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice

#ifndef ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__BUILDER_HPP_
#define ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ackermann_interfaces/msg/detail/ackermann_feedback__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ackermann_interfaces
{

namespace msg
{

namespace builder
{

class Init_AckermannFeedback_right_wheel_speed
{
public:
  explicit Init_AckermannFeedback_right_wheel_speed(::ackermann_interfaces::msg::AckermannFeedback & msg)
  : msg_(msg)
  {}
  ::ackermann_interfaces::msg::AckermannFeedback right_wheel_speed(::ackermann_interfaces::msg::AckermannFeedback::_right_wheel_speed_type arg)
  {
    msg_.right_wheel_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ackermann_interfaces::msg::AckermannFeedback msg_;
};

class Init_AckermannFeedback_left_wheel_speed
{
public:
  explicit Init_AckermannFeedback_left_wheel_speed(::ackermann_interfaces::msg::AckermannFeedback & msg)
  : msg_(msg)
  {}
  Init_AckermannFeedback_right_wheel_speed left_wheel_speed(::ackermann_interfaces::msg::AckermannFeedback::_left_wheel_speed_type arg)
  {
    msg_.left_wheel_speed = std::move(arg);
    return Init_AckermannFeedback_right_wheel_speed(msg_);
  }

private:
  ::ackermann_interfaces::msg::AckermannFeedback msg_;
};

class Init_AckermannFeedback_steering_angle
{
public:
  explicit Init_AckermannFeedback_steering_angle(::ackermann_interfaces::msg::AckermannFeedback & msg)
  : msg_(msg)
  {}
  Init_AckermannFeedback_left_wheel_speed steering_angle(::ackermann_interfaces::msg::AckermannFeedback::_steering_angle_type arg)
  {
    msg_.steering_angle = std::move(arg);
    return Init_AckermannFeedback_left_wheel_speed(msg_);
  }

private:
  ::ackermann_interfaces::msg::AckermannFeedback msg_;
};

class Init_AckermannFeedback_header
{
public:
  Init_AckermannFeedback_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AckermannFeedback_steering_angle header(::ackermann_interfaces::msg::AckermannFeedback::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AckermannFeedback_steering_angle(msg_);
  }

private:
  ::ackermann_interfaces::msg::AckermannFeedback msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ackermann_interfaces::msg::AckermannFeedback>()
{
  return ackermann_interfaces::msg::builder::Init_AckermannFeedback_header();
}

}  // namespace ackermann_interfaces

#endif  // ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__BUILDER_HPP_
