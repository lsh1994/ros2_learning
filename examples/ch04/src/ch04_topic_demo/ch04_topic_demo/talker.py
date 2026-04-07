import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_msgs.msg import String


class TopicTalker(Node):
    def __init__(self):
        super().__init__("topic_talker")
        self.publisher_ = self.create_publisher(String, "demo_chatter", 10)
        self.count = 0
        self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        self.count += 1
        msg = String()
        msg.data = f"hello ros2 {self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"publish: {msg.data}")


def main():
    rclpy.init()
    node = TopicTalker()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
