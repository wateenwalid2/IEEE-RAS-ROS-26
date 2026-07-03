import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import random
count = 0 
class robot_sim_node(Node):
    def __init__(self):
        global count
        count +=1
        super().__init__(f'robot{count}')
        self.pub_pos = self.create_publisher(Pose2D,f"robot{count}/pos",10)
        self.pub_priority = self.create_publisher(Int32,f"robot{count}/priority",10)
        self.timer = self.create_timer(0.1, self.nowPub)
        self.get_logger().info(f"Robot{count} is created")

    def nowPub(self):
        pose = Pose2D()
        pose.x = float(random.randint(0, 20))
        pose.y = float(random.randint(0, 20))
        priority = Int32()
        priority.data = random.randint(1, 10)
        self.pub_pos.publish(pose)
        self.pub_priority.publish(priority)

def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor()
    nodes =[]
    for i in range(1,7):
        node = robot_sim_node()
        nodes.append(node)
        executor.add_node(node)

    executor.spin()
    for node in nodes:
        node.destroy_node()
    
    rclpy.shutdown()
    
    
    

if __name__ == '__main__':
    main()
        


