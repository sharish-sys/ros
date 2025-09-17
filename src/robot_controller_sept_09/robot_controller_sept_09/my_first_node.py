#!/usr/bin/env/python3
import rclpy
from rclpy.node import Node
class MyNode(Node):
    def __init__(self):
        super().__init__("first_node") #super() referene to parent class also called as CONSTRUCTOR
        self.get_logger().info("Helloh from ROSTHCHU")
def main(args=None):
    rclpy.init(args=args)   #initialize rcply
    node = MyNode()
    rclpy.spin(node)    #spin: keeps the node alive, until killed
    rclpy.shutdown()
if __name__=='main': #run only the main function when called
    main()

