// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from ackermann_interfaces:msg/AckermannFeedback.idl
// generated code does not contain a copyright notice

#ifndef ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__FUNCTIONS_H_
#define ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "ackermann_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "ackermann_interfaces/msg/detail/ackermann_feedback__struct.h"

/// Initialize msg/AckermannFeedback message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * ackermann_interfaces__msg__AckermannFeedback
 * )) before or use
 * ackermann_interfaces__msg__AckermannFeedback__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__init(ackermann_interfaces__msg__AckermannFeedback * msg);

/// Finalize msg/AckermannFeedback message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
void
ackermann_interfaces__msg__AckermannFeedback__fini(ackermann_interfaces__msg__AckermannFeedback * msg);

/// Create msg/AckermannFeedback message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * ackermann_interfaces__msg__AckermannFeedback__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
ackermann_interfaces__msg__AckermannFeedback *
ackermann_interfaces__msg__AckermannFeedback__create();

/// Destroy msg/AckermannFeedback message.
/**
 * It calls
 * ackermann_interfaces__msg__AckermannFeedback__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
void
ackermann_interfaces__msg__AckermannFeedback__destroy(ackermann_interfaces__msg__AckermannFeedback * msg);

/// Check for msg/AckermannFeedback message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__are_equal(const ackermann_interfaces__msg__AckermannFeedback * lhs, const ackermann_interfaces__msg__AckermannFeedback * rhs);

/// Copy a msg/AckermannFeedback message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__copy(
  const ackermann_interfaces__msg__AckermannFeedback * input,
  ackermann_interfaces__msg__AckermannFeedback * output);

/// Initialize array of msg/AckermannFeedback messages.
/**
 * It allocates the memory for the number of elements and calls
 * ackermann_interfaces__msg__AckermannFeedback__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__init(ackermann_interfaces__msg__AckermannFeedback__Sequence * array, size_t size);

/// Finalize array of msg/AckermannFeedback messages.
/**
 * It calls
 * ackermann_interfaces__msg__AckermannFeedback__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
void
ackermann_interfaces__msg__AckermannFeedback__Sequence__fini(ackermann_interfaces__msg__AckermannFeedback__Sequence * array);

/// Create array of msg/AckermannFeedback messages.
/**
 * It allocates the memory for the array and calls
 * ackermann_interfaces__msg__AckermannFeedback__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
ackermann_interfaces__msg__AckermannFeedback__Sequence *
ackermann_interfaces__msg__AckermannFeedback__Sequence__create(size_t size);

/// Destroy array of msg/AckermannFeedback messages.
/**
 * It calls
 * ackermann_interfaces__msg__AckermannFeedback__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
void
ackermann_interfaces__msg__AckermannFeedback__Sequence__destroy(ackermann_interfaces__msg__AckermannFeedback__Sequence * array);

/// Check for msg/AckermannFeedback message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__are_equal(const ackermann_interfaces__msg__AckermannFeedback__Sequence * lhs, const ackermann_interfaces__msg__AckermannFeedback__Sequence * rhs);

/// Copy an array of msg/AckermannFeedback messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_ackermann_interfaces
bool
ackermann_interfaces__msg__AckermannFeedback__Sequence__copy(
  const ackermann_interfaces__msg__AckermannFeedback__Sequence * input,
  ackermann_interfaces__msg__AckermannFeedback__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ACKERMANN_INTERFACES__MSG__DETAIL__ACKERMANN_FEEDBACK__FUNCTIONS_H_
