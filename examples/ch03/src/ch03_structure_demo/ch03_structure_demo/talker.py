import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String


class StructureTalker(Node):
    def __init__(self):
        super().__init__("structure_talker")
        self.publisher_ = self.create_publisher(String, "structure_chatter", 10)
        self.count = 0
        self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        self.count += 1
        msg = String()
        msg.data = f"message from package demo #{self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"publish: {msg.data}")


def main():
    rclpy.init()
    node = StructureTalker()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
