// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from my_robot_interfaces:msg/LedStates.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "my_robot_interfaces/msg/detail/led_states__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace my_robot_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void LedStates_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) my_robot_interfaces::msg::LedStates(_init);
}

void LedStates_fini_function(void * message_memory)
{
  auto typed_message = static_cast<my_robot_interfaces::msg::LedStates *>(message_memory);
  typed_message->~LedStates();
}

size_t size_function__LedStates__led_states(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__LedStates__led_states(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<int64_t, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__LedStates__led_states(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<int64_t, 3> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LedStates_message_member_array[1] = {
  {
    "led_states",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(my_robot_interfaces::msg::LedStates, led_states),  // bytes offset in struct
    nullptr,  // default value
    size_function__LedStates__led_states,  // size() function pointer
    get_const_function__LedStates__led_states,  // get_const(index) function pointer
    get_function__LedStates__led_states,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LedStates_message_members = {
  "my_robot_interfaces::msg",  // message namespace
  "LedStates",  // message name
  1,  // number of fields
  sizeof(my_robot_interfaces::msg::LedStates),
  LedStates_message_member_array,  // message members
  LedStates_init_function,  // function to initialize message memory (memory has to be allocated)
  LedStates_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LedStates_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LedStates_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace my_robot_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<my_robot_interfaces::msg::LedStates>()
{
  return &::my_robot_interfaces::msg::rosidl_typesupport_introspection_cpp::LedStates_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, my_robot_interfaces, msg, LedStates)() {
  return &::my_robot_interfaces::msg::rosidl_typesupport_introspection_cpp::LedStates_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif