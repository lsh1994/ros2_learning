import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from std_srvs.srv import Trigger


class StatusServer(Node):
    def __init__(self):
        super().__init__("status_server")
        self.create_service(Trigger, "get_status", self.handle_status)
        self.get_logger().info("Service /get_status is ready.")

    def handle_status(self, request, response):
        del request
        response.success = True
        response.message = "robot is ready"
        self.get_logger().info("Handled /get_status request.")
        return response


def main():
    rclpy.init()
    node = StatusServer()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
