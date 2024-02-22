from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    robot_news_station_node_1 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_1",
        parameters=[
            {"robot_name": "R2D2"}
        ]
    )

    robot_news_station_node_2 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_2",
        parameters=[
            {"robot_name": "Optimus"}
        ]
    )

    robot_news_station_node_3 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_3",
        parameters=[
            {"robot_name": "Bumblebee"}
        ]
    )

    robot_news_station_node_4 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_4",
        parameters=[
            {"robot_name": "IronHide"}
        ]
    )

    robot_news_station_node_5 = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="robot_news_station_5",
        parameters=[
            {"robot_name": "Sentinel"}
        ]
    )

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
    )

    ld.add_action(robot_news_station_node_1)
    ld.add_action(robot_news_station_node_2)
    ld.add_action(robot_news_station_node_3)
    ld.add_action(robot_news_station_node_4)
    ld.add_action(robot_news_station_node_5)
    ld.add_action(smartphone_node)
    return ld