import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String


class TopicListener(Node):
    def __init__(self):
        super().__init__("topic_listener")
        self.create_subscription(String, "demo_chatter", self.on_message, 10)

    def on_message(self, msg):
        self.get_logger().info(f"receive: {msg.data}")


def main():
    rclpy.init()
    node = TopicListener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
