import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class AutonomousMover(Node):
    def __init__(self):
        super().__init__('autonomous_mover')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_robot)
        self.get_logger().info('start moving')

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.5 
        msg.linear.y = 0.5 
        msg.angular.z = 0.1 
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
