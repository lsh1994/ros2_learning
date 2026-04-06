import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String


class StructureListener(Node):
    def __init__(self):
        super().__init__("structure_listener")
        self.create_subscription(String, "structure_chatter", self.on_message, 10)

    def on_message(self, msg):
        self.get_logger().info(f"receive: {msg.data}")


def main():
    rclpy.init()
    node = StructureListener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
