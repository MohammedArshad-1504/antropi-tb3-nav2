import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    # ---------------------------------------------------------
    # Package locations
    # ---------------------------------------------------------

    pkg_antropi = get_package_share_directory(
        'antropi_tb3_nav'
    )

    pkg_tb3 = get_package_share_directory(
        'turtlebot3_gazebo'
    )

    pkg_ros_gz_sim = get_package_share_directory(
        'ros_gz_sim'
    )


    # ---------------------------------------------------------
    # Custom world
    # ---------------------------------------------------------

    world_file = os.path.join(
        pkg_antropi,
        'worlds',
        'antropi_world.sdf'
    )


    # ---------------------------------------------------------
    # Gazebo
    # ---------------------------------------------------------

    gazebo = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_ros_gz_sim,
                'launch',
                'gz_sim.launch.py'
            )
        ),

        launch_arguments={
            'gz_args': f'-r -v2 {world_file}',
            'on_exit_shutdown': 'true'
        }.items()
    )


    # ---------------------------------------------------------
    # TurtleBot3 robot_state_publisher
    # ---------------------------------------------------------

    robot_state_publisher = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_tb3,
                'launch',
                'robot_state_publisher.launch.py'
            )
        ),

        launch_arguments={
            'use_sim_time': 'true'
        }.items()
    )


    # ---------------------------------------------------------
    # Spawn TurtleBot3
    #
    # Central area
    # Clear of the central obstacles
    # ---------------------------------------------------------

    spawn_robot = IncludeLaunchDescription(

        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_tb3,
                'launch',
                'spawn_turtlebot3.launch.py'
            )
        ),

        launch_arguments={
            'x_pose': '-2.5',
            'y_pose': '0.0',
            'z_pose': '0.1'
        }.items()
    )


    # ---------------------------------------------------------
    # Launch everything
    # ---------------------------------------------------------

    return LaunchDescription([

        AppendEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            os.path.join(
                pkg_tb3,
                'models'
            )
        ),

        gazebo,

        robot_state_publisher,

        spawn_robot,

    ])
