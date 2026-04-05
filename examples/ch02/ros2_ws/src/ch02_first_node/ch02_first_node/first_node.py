import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class FirstNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.count = 0
        self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        self.count += 1
        self.get_logger().info(f"Hello ROS 2, count={self.count}")


def main():
    rclpy.init()
    node = FirstNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()