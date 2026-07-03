import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('safety_zone', default_value='2.0'),
        DeclareLaunchArgument('robot_priority', default_value='5'),
        DeclareLaunchArgument('robot_position', default_value='[10.0, 10.0]'),

        Node(
            package='fleet_package',  
            executable='fleet_emulator',
            name='fleet_emulator',
            output='screen'
        ),

        Node(
            package='fleet_package',  
            executable='fleet_traffic_manager', 
            name='fleet_traffic_manager',
            output='screen',
            parameters=[{
                'safety_zone': LaunchConfiguration('safety_zone'),
                'robot_priority': LaunchConfiguration('robot_priority'),
                'robot_position': LaunchConfiguration('robot_position'),
            }]
        )
    ])