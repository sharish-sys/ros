#!/usr/bin/env/python3
import rclpy
from rclpy.node import Node
class MyNode(Node):
    def __init__(self):
        super().__init__("first node")#super() referene to parent class 
def main(args=None):
    rclpy.init(args=args)#initialize rcply
    rclpy.shutdown()
if __name__=='main': #run only the main function when called
    main()

