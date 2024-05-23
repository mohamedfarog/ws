// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice

#ifndef ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__TRAITS_HPP_
#define ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ackermann_interfaces/msg/detail/ackermann_feedback__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace ackermann_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const AckermannFeedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: steering_angle
  {
    out << "steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle, out);
    out << ", ";
  }

  // member: left_wheel_speed
  {
    out << "left_wheel_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.left_wheel_speed, out);
    out << ", ";
  }

  // member: right_wheel_speed
  {
    out << "right_wheel_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.right_wheel_speed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AckermannFeedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: steering_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "steering_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.steering_angle, out);
    out << "\n";
  }

  // member: left_wheel_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_wheel_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.left_wheel_speed, out);
    out << "\n";
  }

  // member: right_wheel_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_wheel_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.right_wheel_speed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AckermannFeedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ackermann_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use ackermann_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ackermann_interfaces::msg::AckermannFeedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  ackermann_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ackermann_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const ackermann_interfaces::msg::AckermannFeedback & msg)
{
  return ackermann_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ackermann_interfaces::msg::AckermannFeedback>()
{
  return "ackermann_interfaces::msg::AckermannFeedback";
}

template<>
inline const char * name<ackermann_interfaces::msg::AckermannFeedback>()
{
  return "ackermann_interfaces/msg/AckermannFeedback";
}

template<>
struct has_fixed_size<ackermann_interfaces::msg::AckermannFeedback>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<ackermann_interfaces::msg::AckermannFeedback>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<ackermann_interfaces::msg::AckermannFeedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__TRAITS_HPP_
