#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node): 
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self): #Timer sayesinde bir düğüm istenilen frekans aralığında çalıştırılabilir.
        self.counter_ +=1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args) #İletişim başlat 
    #Düğüm oluştur 
    #Düğüm adı ile dosya adı farklı olabilir  
    #Düğüm adı ile executable adı farklı olabilir.
    node=MyNode() #Düğüm ile bilgi gönder
    rclpy.spin(node) 
    #Spin komutu ile program bu noktada durur ve düğümü açık tutar. İleride publisher, subscriber ve service eklendiğinde callback fonksiyonları spin fonksiyonu tarafından tanımlanır
    rclpy.shutdown() #İletişimi bitir

if __name__ == "__main__":
    main()