import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher

from sensor_msgs.msg import PointCloud2


class SimToVelodyne(Node):
    def __init__(self):
        super().__init__("velodyne_translator_node")

        # subscriber to lidar
        self.create_subscription(PointCloud2, "/fsds/lidar/Lidar2", self.callback, 1)

        # publishers for split pose and velocity
        self.pointcloud_publisher: Publisher = self.create_publisher(PointCloud2, "/velodyne_points", 1)

        self.get_logger().info("---Sim pointcloud translator initialised---")

    def callback(self, pointcloud_msg: PointCloud2):
        pub_msg = pointcloud_msg
        pub_msg.header.frame_id = "velodyne"
        self.pointcloud_publisher.publish(pub_msg)


def main(args=None):
    rclpy.init(args=args)
    node = SimToVelodyne()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
