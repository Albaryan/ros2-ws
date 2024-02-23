#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from std_srvs.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_=0
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        
        self.publisher_ = self.create_publisher(Int64,"number_count",10)
        
        self.server_=self.create_service(SetBool,"reset_number_count",self.callback_reset_number_count)

        self.get_logger().info("Number counting has started")

    def callback_number(self, msg):
        self.counter_+=msg.data
        new_msg=Int64()
        new_msg.data=self.counter_
        self.publisher_.publish(new_msg)

    def callback_reset_number_count(self, request, response):
        if request.data:
            self.counter_=0
            response.success=True
            response.message="Counter reset!"
        return response
            


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__=="__main__":
    main()