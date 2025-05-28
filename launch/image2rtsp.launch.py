import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
   rgb_config = os.path.join(
      get_package_share_directory('image2rtsp'),
      'config',
      'rgb_parameters.yaml'
      )
   
   ir_config = os.path.join(
      get_package_share_directory('image2rtsp'),
      'config',
      'ir_parameters.yaml'
      )

   return LaunchDescription([
      # Node(
      #    package='image2rtsp',
      #    executable='image2rtsp',
      #    namespace='rgb_camera',
      #    name='image2rtsp',
      #    parameters=[rgb_config],
      #    output='screen',
      # ),
      Node(
         package='image2rtsp',
         executable='image2rtsp',
         # namespace='ir_camera',
         name='image2rtsp',
         parameters=[ir_config],
         output='screen',
      )
   ])