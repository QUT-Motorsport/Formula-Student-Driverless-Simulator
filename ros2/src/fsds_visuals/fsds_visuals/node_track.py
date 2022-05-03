# import ROS2 libraries
import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
# import ROS2 message libraries
from visualization_msgs.msg import Marker, MarkerArray
from builtin_interfaces.msg import Duration
# import custom message libraries
from fs_msgs.msg import Track

# other python modules
from typing import List


def marker_msg(
    colour: int, 
    x_coord: float, 
    y_coord: float, 
    ID: int, 
) -> Marker: 
    """
    Creates a Marker object for cones or a car.
    * param colour: Cone.COLOR
    * param x_coord: x position relative to parent frame
    * param y_coord: y position relative to parent frame
    * param ID: Unique for markers in the same frame
    * param header: passed in because creating time is dumb
    * return: Marker
    """

    marker = Marker()
    marker.header.frame_id = "map"
    marker.ns = "current_scan"
    marker.id = ID
    marker.type = Marker.CYLINDER
    marker.action = Marker.ADD

    marker.pose.position.x = x_coord
    marker.pose.position.y = y_coord
    marker.pose.position.z = 0.16
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    # scale out of 1x1x1m
    marker.scale.x = 0.228
    marker.scale.y = 0.228
    marker.scale.z = 0.32

    if colour == 0: # blue cone
        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0
    elif colour == 1: # yellow cone
        marker.color.r = 0.901
        marker.color.g = 0.858
        marker.color.b = 0.039
    elif colour == 2: # orange cone
        marker.color.r = 0.901
        marker.color.g = 0.309
        marker.color.b = 0.039
        marker.pose.position.z = 0.225 # is taller
        marker.scale.z = 0.45
    marker.color.a = 1.0 # alpha
    
    marker.lifetime = Duration(sec=10, nanosec=100000)

    return marker


class SimVisualiser(Node):
    def __init__(self):
        super().__init__('sim_visualiser')

        # sub to track for all cone locations relative to car start point
        self.create_subscription(Track, "/testing_only/track", self.map_callback, 10)

        # publishes rviz cone markers
        self.cone_publisher: Publisher = self.create_publisher(MarkerArray, "/fsds_visuals/track_cones", 1)


    def map_callback(self, track_msg: Track):       
        # track cone list is taken as coords relative to the initial car position
        self.track = track_msg.track

        markers_list: List[Marker] = []
        for i, cone in enumerate(track_msg.track):
            # add on each cone to published array
            marker: Marker = marker_msg(
                cone.color,
                cone.location.x, 
                cone.location.y, 
                i, 
            )
            marker.header.stamp = self.get_clock().now().to_msg()
            markers_list.append(marker)

        # create message for all cones on the track
        markers_msg = MarkerArray(markers=markers_list)
        self.cone_publisher.publish(markers_msg) # publish marker points data


def main():
    # begin ros node
    rclpy.init()

    node = SimVisualiser()
    rclpy.spin(node)
    
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()