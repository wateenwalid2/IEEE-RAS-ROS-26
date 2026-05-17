import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math
from functools import partial 

class FleetTrafficManager(Node):
    def __init__(self):
        super().__init__('fleet_traffic_manager')
        self.my_x = 10.0
        self.my_y = 10.0
        self.my_priority = 5
        self.safety_zone = 2.0 
        self.fleet_data = {} 

        for i in range(1,7): 
            self.fleet_data[i] = {'pose': None, 'priority': None}
            self.create_subscription(Pose2D, f'robot{i}/pos', partial(self.pose_callback, robot_name = i), 10)
            self.create_subscription(Int32, f'robot{i}/priority', partial(self.priority_callback, robot_name = i), 10)

        self.create_timer(1, self.check_all_fleet)
        self.get_logger().info('Traffic manager is created')

    def pose_callback(self, msg, robot_name):
        self.fleet_data[robot_name]['pose'] = msg

    def priority_callback(self, msg, robot_name):
        self.fleet_data[robot_name]['priority'] = msg.data

    def check_all_fleet(self):
        danger = False
        for robot_name, data in self.fleet_data.items():
            if ((data['pose'] is None) or (data['priority'] is None)):
                continue
            distance = math.sqrt(((data['pose'].x - self.my_x)**2) + ((data['pose'].y - self.my_y)**2))

            if ((distance < self.safety_zone) and (data['priority'] > self.my_priority)):
                self.get_logger().info(f'[DANGER] robot{robot_name} is too close (the distance from you is {distance}) with Priority {data["priority"]}!')
                danger = True
                break 
        if not danger:
            self.get_logger().info('[CLEAR] No immediate threats from the fleet')

def main(args=None):
    rclpy.init(args=args)
    node = FleetTrafficManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()