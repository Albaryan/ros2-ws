#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
import time

from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        while True:
            self.call_set_led_server(0,True)
            time.sleep(4)
            self.call_set_led_server(3,False)
            time.sleep(6)



        
    def call_set_led_server(self,led_number,state):
        client = self.create_client(SetLed, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server LedStates...")
        
        request = SetLed.Request()
        request.led_number=led_number
        request.state=state

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led,led_number=led_number,state=state))

    def callback_call_set_led(self, future, led_number, state):
        try:
            response = future.result()
            self.get_logger().info("Success = "+str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__=="__main__":
    main()