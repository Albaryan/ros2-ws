#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedStates

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel_node")
        self.server_ = self.create_service(SetLed,"set_led", self.callback_add_two_ints)
        self.led_states_ = [0,0,0]
        self.publisher_ = self.create_publisher(LedStates, "led_panel_state", 10)
        self.timer_ = self.create_timer(0.5, self.publish_led_states)
        self.get_logger().info("Led states publishing...")


    def callback_add_two_ints(self, request, response):
        response.success = True


        

        if request.state:
            self.led_states_[request.led_number-1]=1
        elif not request.state:
            self.led_states_=[0,0,0]

        self.get_logger().info("Success is "+ str(response.success))
        return response
    
    def publish_led_states(self):
        msg=LedStates()
        msg.led_states = self.led_states_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__=="__main__":
    main()