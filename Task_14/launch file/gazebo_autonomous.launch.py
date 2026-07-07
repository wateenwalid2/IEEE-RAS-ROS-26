import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, AppendEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'autonomous_robot_sim'
    pkg_share = get_package_share_directory(package_name)
    

    sdf_world_path = os.path.join(pkg_share, 'worlds', 'first.sdf')


    tb3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    models_path = os.path.join(tb3_gazebo_dir, 'models')
    robot_model_path = os.path.join(models_path, 'turtlebot3_burger', 'model.sdf')


    set_model_path = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        models_path
    )

    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', sdf_world_path, '-r'],
        output='screen'
    )

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'turtlebot3_burger',
            '-file', robot_model_path,
            '-x', '-3',
            '-y', '-3',
            '-z', '0.3'
        ],
        output='screen'
    )


    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/model/turtlebot3_burger/odometry@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/world/empty/model/turtlebot3_burger/link/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'
        ],
        output='screen'
    )

    mover_node = Node(
        package=package_name,
        executable='autonomous_mover.py',
        output='screen'
    )

    return LaunchDescription([
        set_model_path,
        gazebo,
        spawn_robot,
        ros_gz_bridge,
        mover_node
    ])