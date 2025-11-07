import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePub(Node):
    def __init__(self):
        super().__init__('simple_node')
        self.publisher = self.create_publisher(String, '/hello', 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "hello this is my first publisher"
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main():
    rclpy.init()
    simple_pub = SimplePub()
    rclpy.spin(simple_pub)
    simple_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
