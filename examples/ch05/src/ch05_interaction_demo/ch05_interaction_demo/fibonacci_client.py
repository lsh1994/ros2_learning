import sys

import rclpy
from example_interfaces.action import Fibonacci
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class FibonacciClient(Node):
    def __init__(self):
        super().__init__("fibonacci_client")
        self._client = ActionClient(self, Fibonacci, "fibonacci")
        self._done = False

    def send_goal(self, order):
        goal = Fibonacci.Goal()
        goal.order = order
        self._client.wait_for_server()
        future = self._client.send_goal_async(goal, feedback_callback=self.feedback_callback)
        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected.")
            self._done = True
            return
        self.get_logger().info("Goal accepted.")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(
            f"feedback: {list(feedback_msg.feedback.sequence)}"
        )

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"result: {list(result.sequence)}")
        self._done = True


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciClient()
    order = 8
    if len(sys.argv) > 1:
        order = int(sys.argv[1])
    node.send_goal(order)
    try:
        while rclpy.ok() and not node._done:
            rclpy.spin_once(node, timeout_sec=0.1)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
