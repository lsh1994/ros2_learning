import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException


class ParamNode(Node):
    def __init__(self):
        super().__init__("param_node")
        self.declare_parameter("rate", 1.0)
        self.declare_parameter("robot_name", "demo_bot")
        self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        rate = self.get_parameter("rate").value
        robot_name = self.get_parameter("robot_name").value
        self.get_logger().info(f"robot_name={robot_name}, rate={rate}")


def main():
    rclpy.init()
    node = ParamNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
