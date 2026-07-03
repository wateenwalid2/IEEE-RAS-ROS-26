import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math
from functools import partial 

class FleetTrafficManager(Node):
    def __init__(self):
        super().__init__('fleet_traffic_manager')
        self.declare_parameter('robot_position', [10.0, 10.0])
        self.declare_parameter('robot_priority', 5)
        self.declare_parameter('safety_zone', 2.0)

        self.fleet_data = {} 

        for i in range(1, 7): 
            self.fleet_data[i] = {'pose': None, 'priority': None}
            self.create_subscription(Pose2D, f'robot{i}/pos', partial(self.pose_callback, robot_name=i), 10)
            self.create_subscription(Int32, f'robot{i}/priority', partial(self.priority_callback, robot_name=i), 10)

        self.create_timer(1, self.check_all_fleet)
        self.get_logger().info('Traffic manager is created')

    def pose_callback(self, msg, robot_name):
        self.fleet_data[robot_name]['pose'] = msg

    def priority_callback(self, msg, robot_name):
        self.fleet_data[robot_name]['priority'] = msg.data

    def check_all_fleet(self):
        safety_zone = self.get_parameter('safety_zone').get_parameter_value().double_value
        my_priority = self.get_parameter('robot_priority').get_parameter_value().integer_value
        robot_position_param = self.get_parameter('robot_position').get_parameter_value().double_array_value
        
        my_x = robot_position_param[0]
        my_y = robot_position_param[1]
        danger = False
        
        for robot_name, data in self.fleet_data.items():
            if (data['pose'] is None) or (data['priority'] is None):
                continue
            
            distance = math.sqrt(((data['pose'].x - my_x)**2) + ((data['pose'].y - my_y)**2))

            if (distance < safety_zone) and (data['priority'] > my_priority):
                self.get_logger().info(f'[DANGER] robot{robot_name} is too close (the distance from you is {distance:.2f}) with Priority {data["priority"]}!')
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