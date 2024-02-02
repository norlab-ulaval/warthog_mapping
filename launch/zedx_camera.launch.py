import os, yaml

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    script = os.path.join(get_package_share_directory('warthog_mapping'), 'scripts', "start_zed.sh")
    zed_camera_node = ExecuteProcess(
        name="zed_camera_node",
        cmd=[[f"bash {script}"]],
        output='screen',
        shell=True
    )

    return LaunchDescription([
        zed_camera_node         
    ])