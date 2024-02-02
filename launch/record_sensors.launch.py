import os, yaml

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    config_folder = os.path.join(get_package_share_directory('warthog_mapping'), 'params')
    topics_file = os.path.join(config_folder, 'topics_to_record.yaml')

    topics_list = yaml.safe_load(open(topics_file, 'r'))["topics"]
    command = ['ros2', 'bag', 'record', '-s', 'mcap']
    command.extend(topics_list)

    sensors_record_process = ExecuteProcess(
        name="rosbag_record",
        cmd=command,
        output='screen'
    )

    script = os.path.join(get_package_share_directory('warthog_mapping'), 'scripts', "record_zed.sh")
    zed_record_process = ExecuteProcess(
        name="zed_record_node",
        cmd=[[f"bash {script}"]],
        output='screen',
        shell=True
    )

    return LaunchDescription([
        sensors_record_process,
        zed_record_process         
    ])