# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mini_ugv_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mini_ugv_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mini_ugv_FOUND FALSE)
  elseif(NOT mini_ugv_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mini_ugv_FOUND FALSE)
  endif()
  return()
endif()
set(_mini_ugv_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mini_ugv_FIND_QUIETLY)
  message(STATUS "Found mini_ugv: 0.0.0 (${mini_ugv_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mini_ugv' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mini_ugv_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mini_ugv_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mini_ugv_DIR}/${_extra}")
endforeach()