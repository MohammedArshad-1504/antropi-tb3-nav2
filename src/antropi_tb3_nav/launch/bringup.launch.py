import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import SetParameter
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_antropi = get_package_share_directory('antropi_tb3_nav')

    # Gazebo + TurtleBot3
    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_antropi,
                'launch',
                'sim.launch.py'
            )
        )
    )

    # Nav2 configuration
    map_file = os.path.join(
        pkg_antropi,
        'maps',
        'antropi_map.yaml'
    )

    params_file = os.path.join(
        pkg_antropi,
        'config',
        'nav2_params.yaml'
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('nav2_bringup'),
                'launch',
                'bringup_launch.py'
            )
        ),
        launch_arguments={
            'map': map_file,
            'use_sim_time': 'true',
            'params_file': params_file,
        }.items()
    )

    return LaunchDescription([
        SetParameter(
            name='use_sim_time',
            value=True
        ),

        sim_launch,
        nav2_launch,
    ])
