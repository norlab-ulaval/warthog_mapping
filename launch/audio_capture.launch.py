from launch.actions import DeclareLaunchArgument
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    _dst = LaunchConfiguration('dst')
    _device = LaunchConfiguration('capture_device')
    _format = LaunchConfiguration('format')
    _bitrate = LaunchConfiguration('bitrate')
    _channels = LaunchConfiguration('channels')
    _depth = LaunchConfiguration('depth')
    _sample_rate = LaunchConfiguration('sample_rate')
    _sample_format = LaunchConfiguration('sample_format')
    _ns = LaunchConfiguration('ns')
    _audio_topic = LaunchConfiguration('audio_topic')

    _dst_launch_arg = DeclareLaunchArgument(
        'dst',
        default_value='appsink'
    )
    _device_launch_arg = DeclareLaunchArgument(
        'capture_device',
        default_value=''
    )
    _format_launch_arg = DeclareLaunchArgument(
        'format',
        default_value='mp3'
    )
    _bitrate_launch_arg = DeclareLaunchArgument(
        'bitrate',
        default_value='128'
    )
    _channels_launch_arg = DeclareLaunchArgument(
        'channels',
        default_value='1'
    )
    _depth_launch_arg = DeclareLaunchArgument(
        'depth',
        default_value='16'
    )
    _sample_rate_launch_arg = DeclareLaunchArgument(
        'sample_rate',
        default_value='16000'
    )
    _sample_format_launch_arg = DeclareLaunchArgument(
        'sample_format',
        default_value='S16LE'
    )
    _ns_launch_arg = DeclareLaunchArgument(
        'ns',
        default_value='audio'
    )
    _audio_topic_launch_arg = DeclareLaunchArgument(
        'audio_topic',
        default_value='audio'
    )

    _audio_capture_node = Node(
        package='audio_capture',
        name='audio_capture',
        executable='audio_capture_node',
        namespace=_ns,
        remappings=[
            ('audio', _audio_topic),
        ],
        parameters=[{
            'dst': _dst,
            'device': _device,
            'format': _format,
            'bitrate': _bitrate,
            'channels': _channels,
            'depth': _depth,
            'sample_rate': _sample_rate,
            'sample_format': _sample_format,
        }],
    )

    return LaunchDescription([
        _dst_launch_arg,
        _device_launch_arg,
        _format_launch_arg,
        _bitrate_launch_arg,
        _channels_launch_arg,
        _depth_launch_arg,
        _sample_rate_launch_arg,
        _sample_format_launch_arg,
        _ns_launch_arg,
        _audio_topic_launch_arg,
        _audio_capture_node,
    ])
