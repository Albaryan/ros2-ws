#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
from geometry_msgs.msg import Twist
import cv2


class CameraAndControlNode(Node):
    def __init__(self):
        super().__init__("camera_n_control")
        self.subscriber_ = self.create_subscription(Image, "/camera/image_raw", self.callback_camera_n_control, 10)
        
        self.bridge = CvBridge()
        
        self.vel=Twist()
        
        self.publisher_= self.create_publisher(Twist, "/cmd_vel",10)
        
        self.get_logger().info("Control from camera has started.")

    def callback_camera_n_control(self, msg):
        
        try:
            cv_image = cv2.resize(self.bridge.imgmsg_to_cv2(msg,'bgr8'),None, fx=1/2,fy=1/2,interpolation=cv2.INTER_LINEAR)
        except CvBridgeError as e:
            print(e)
            
        cv2.imshow("img",cv_image)
        
        key=cv2.waitKey(1)
        
        if key==ord('w'):
            self.vel.linear.x+=0.5
            self.publisher_.publish(self.vel)
            
        elif key==ord('a'):
            self.vel.angular.z+=0.5
            self.publisher_.publish(self.vel)
            
        elif key==ord('s'):
            self.vel.linear.x-=0.5
            self.publisher_.publish(self.vel)
            
        elif key==ord('d'):
            self.vel.angular.z-=0.5
            self.publisher_.publish(self.vel)
            
        elif key==ord(' '):
            self.vel=Twist()
            self.publisher_.publish(self.vel)
            


def main(args=None):
    rclpy.init(args=args)
    node = CameraAndControlNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__=="__main__":
    main()