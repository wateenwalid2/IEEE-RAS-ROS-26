import rclpy
from rclpy.node import Node
import math
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

class TrafficManager(Node):
    def __init__(self):
        super().__init__('traffic_manager')
        self.my_x = 4.5
        self.my_y = 3.0
        self.my_theta = 2.3
        self.my_priority = 3  
        self.safety_zone = 2.5 

        self.robots_incoming_data = {}

        tracked_robots = ['robot1', 'robot2', 'robot3']

        for robot in tracked_robots:
            self.robots_incoming_data[robot] = {'x': None, 'y': None, 'theta': None,'priority': None}

            self.create_subscription(Pose2D, f'/{robot}/pose', lambda msg, r=robot: self.pose_callback(msg, r), 10)
            self.create_subscription(Int32, f'/{robot}/priority',lambda msg, r=robot: self.priority_callback(msg, r), 10)
            
        self.control_timer = self.create_timer(0.1, self.take_decision)

    
    def pose_callback(self, msg, robot_name):
        self.robots_incoming_data[robot_name]['x'] = msg.x
        self.robots_incoming_data[robot_name]['y'] = msg.y
        self.robots_incoming_data[robot_name]['theta'] = msg.theta

    def priority_callback(self, msg, robot_name):
        self.robots_incoming_data[robot_name]['priority'] = msg.data

    def take_decision(self):
        danger_detected = False

        for robot_name, data in self.robots_incoming_data.items():
            if data['x'] is None or data['priority'] is None:
                continue

            distance = math.sqrt((data['x'] - self.my_x)**2 + (data['y'] - self.my_y)**2)

            if distance <= self.safety_zone and data['priority'] > self.my_priority:
                danger_detected = True
                break 

        if danger_detected:
            self.get_logger().info(f'[DANGER] {robot_name} is too close (the distance from you is {distance}) with Priority {data["priority"]}!')
        else:
            self.get_logger().info('[CLEAR] No threat detected')

def main(args=None):
    rclpy.init(args=args)
    node = TrafficManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()