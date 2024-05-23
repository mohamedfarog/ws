// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice

#ifndef ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_H_
#define ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/AckermannFeedback in the package ackermann_interfaces.
typedef struct ackermann_interfaces__msg__AckermannFeedback
{
  std_msgs__msg__Header header;
  float steering_angle;
  float left_wheel_speed;
  float right_wheel_speed;
} ackermann_interfaces__msg__AckermannFeedback;

// Struct for a sequence of ackermann_interfaces__msg__AckermannFeedback.
typedef struct ackermann_interfaces__msg__AckermannFeedback__Sequence
{
  ackermann_interfaces__msg__AckermannFeedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ackermann_interfaces__msg__AckermannFeedback__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__STRUCT_H_
