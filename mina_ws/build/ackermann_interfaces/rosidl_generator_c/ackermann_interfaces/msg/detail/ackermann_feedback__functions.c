// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice
#include "ackermann_interfaces/msg/detail/ackermann_feedback__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
ackermann_interfaces__msg__AckermannFeedback__init(ackermann_interfaces__msg__AckermannFeedback * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    ackermann_interfaces__msg__AckermannFeedback__fini(msg);
    return false;
  }
  // steering_angle
  // left_wheel_speed
  // right_wheel_speed
  return true;
}

void
ackermann_interfaces__msg__AckermannFeedback__fini(ackermann_interfaces__msg__AckermannFeedback * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // steering_angle
  // left_wheel_speed
  // right_wheel_speed
}

bool
ackermann_interfaces__msg__AckermannFeedback__are_equal(const ackermann_interfaces__msg__AckermannFeedback * lhs, const ackermann_interfaces__msg__AckermannFeedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // steering_angle
  if (lhs->steering_angle != rhs->steering_angle) {
    return false;
  }
  // left_wheel_speed
  if (lhs->left_wheel_speed != rhs->left_wheel_speed) {
    return false;
  }
  // right_wheel_speed
  if (lhs->right_wheel_speed != rhs->right_wheel_speed) {
    return false;
  }
  return true;
}

bool
ackermann_interfaces__msg__AckermannFeedback__copy(
  const ackermann_interfaces__msg__AckermannFeedback * input,
  ackermann_interfaces__msg__AckermannFeedback * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // steering_angle
  output->steering_angle = input->steering_angle;
  // left_wheel_speed
  output->left_wheel_speed = input->left_wheel_speed;
  // right_wheel_speed
  output->right_wheel_speed = input->right_wheel_speed;
  return true;
}

ackermann_interfaces__msg__AckermannFeedback *
ackermann_interfaces__msg__AckermannFeedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ackermann_interfaces__msg__AckermannFeedback * msg = (ackermann_interfaces__msg__AckermannFeedback *)allocator.allocate(sizeof(ackermann_interfaces__msg__AckermannFeedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ackermann_interfaces__msg__AckermannFeedback));
  bool success = ackermann_interfaces__msg__AckermannFeedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ackermann_interfaces__msg__AckermannFeedback__destroy(ackermann_interfaces__msg__AckermannFeedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ackermann_interfaces__msg__AckermannFeedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__init(ackermann_interfaces__msg__AckermannFeedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ackermann_interfaces__msg__AckermannFeedback * data = NULL;

  if (size) {
    data = (ackermann_interfaces__msg__AckermannFeedback *)allocator.zero_allocate(size, sizeof(ackermann_interfaces__msg__AckermannFeedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ackermann_interfaces__msg__AckermannFeedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ackermann_interfaces__msg__AckermannFeedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ackermann_interfaces__msg__AckermannFeedback__Sequence__fini(ackermann_interfaces__msg__AckermannFeedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ackermann_interfaces__msg__AckermannFeedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ackermann_interfaces__msg__AckermannFeedback__Sequence *
ackermann_interfaces__msg__AckermannFeedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ackermann_interfaces__msg__AckermannFeedback__Sequence * array = (ackermann_interfaces__msg__AckermannFeedback__Sequence *)allocator.allocate(sizeof(ackermann_interfaces__msg__AckermannFeedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ackermann_interfaces__msg__AckermannFeedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ackermann_interfaces__msg__AckermannFeedback__Sequence__destroy(ackermann_interfaces__msg__AckermannFeedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ackermann_interfaces__msg__AckermannFeedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__are_equal(const ackermann_interfaces__msg__AckermannFeedback__Sequence * lhs, const ackermann_interfaces__msg__AckermannFeedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ackermann_interfaces__msg__AckermannFeedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__copy(
  const ackermann_interfaces__msg__AckermannFeedback__Sequence * input,
  ackermann_interfaces__msg__AckermannFeedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ackermann_interfaces__msg__AckermannFeedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ackermann_interfaces__msg__AckermannFeedback * data =
      (ackermann_interfaces__msg__AckermannFeedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ackermann_interfaces__msg__AckermannFeedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ackermann_interfaces__msg__AckermannFeedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ackermann_interfaces__msg__AckermannFeedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
