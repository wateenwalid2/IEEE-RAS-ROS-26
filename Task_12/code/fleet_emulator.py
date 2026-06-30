import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

robots = {
            'robot1': {'x': 2.5, 'y': 2.5, 'theta': 2.5,'priority': 5,},
            'robot2': {'x': 0.5, 'y': 0.5, 'theta': 0.5 ,'priority': 2,},
            'robot3': {'x': 4.0, 'y': 1.0, 'theta': 0.5 ,'priority': 4,}
        }
class FleetEmulator(Node):
    def __init__(self,robot_name, robot_data):
        super().__init__(f'{robot_name}')
        self.robot_name = robot_name
        self.robot_data = robot_data
 
        self.pose_pub = self.create_publisher(Pose2D, f'/{robot_name}/pose', 10)
        self.priority_pub = self.create_publisher(Int32, f'/{robot_name}/priority', 10)

        self.timer = self.create_timer(0.1, self.call_back)
    
    def call_back(self):
        pose_msg = Pose2D()
        pose_msg.x = self.robot_data['x']
        pose_msg.y = self.robot_data['y']
        pose_msg.theta = self.robot_data['theta']
        self.pose_pub.publish(pose_msg)

        priority_msg = Int32()
        priority_msg.data = self.robot_data['priority']
        self.priority_pub.publish(priority_msg)
def main(args=None):
    rclpy.init(args=args)
    executor = SingleThreadedExecutor()
    nodes = []
    for robot_name, robot_data in robots.items():
        node = FleetEmulator(robot_name, robot_data)
        executor.add_node(node)
        nodes.append(node)
        
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        for node in nodes:
            node.destroy_node()

        rclpy.shutdown()

if __name__ == '__main__':
    main()
