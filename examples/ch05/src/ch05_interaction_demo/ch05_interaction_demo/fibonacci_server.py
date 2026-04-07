import time

import rclpy
from example_interfaces.action import Fibonacci
from rclpy.action import ActionServer
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class FibonacciServer(Node):
    def __init__(self):
        super().__init__("fibonacci_server")
        self._server = ActionServer(
            self,
            Fibonacci,
            "fibonacci",
            self.execute_callback,
        )
        self.get_logger().info("Action /fibonacci is ready.")

    def execute_callback(self, goal_handle):
        order = max(goal_handle.request.order, 0)
        self.get_logger().info(f"Executing fibonacci with order={order}")

        if order == 0:
            sequence = [0]
        elif order == 1:
            sequence = [0, 1]
        else:
            sequence = [0, 1]
            for _ in range(2, order + 1):
                if not goal_handle.is_active:
                    self.get_logger().info("Goal is no longer active.")
                    result = Fibonacci.Result()
                    result.sequence = sequence
                    return result
                sequence.append(sequence[-1] + sequence[-2])
                feedback = Fibonacci.Feedback()
                feedback.sequence = sequence
                goal_handle.publish_feedback(feedback)
                time.sleep(0.3)

        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = sequence
        return result


def main():
    rclpy.init()
    node = FibonacciServer()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
