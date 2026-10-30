from setuptools import find_packages, setup
from glob import glob
import os


package_name = 'antropi_tb3_nav'


setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(
        exclude=['test']
    ),

    data_files=[

        # ROS 2 package index
        (
            'share/ament_index/resource_index/packages',
            [
                'resource/' + package_name
            ]
        ),

        # package.xml
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Launch files
        (
            os.path.join(
                'share',
                package_name,
                'launch'
            ),
            glob('launch/*.py')
        ),

        # Gazebo worlds
        (
            os.path.join(
                'share',
                package_name,
                'worlds'
            ),
            glob('worlds/*')
        ),

        # Navigation configuration
        (
            os.path.join(
                'share',
                package_name,
                'config'
            ),
            glob('config/*')
        ),

        # Maps
        (
            os.path.join(
                'share',
                package_name,
                'maps'
            ),
            glob('maps/*')
        ),

        # RViz configurations
        (
            os.path.join(
                'share',
                package_name,
                'rviz'
            ),
            glob('rviz/*')
        ),

    ],

    install_requires=[
        'setuptools',
    ],

    zip_safe=True,

    maintainer='mohammed-arshad-s',

    maintainer_email='md.arshad1504@gmail.com',

    description='Custom TurtleBot3 Gazebo world and Nav2 configuration for the Antropi Robotics assignment',

    license='Apache-2.0',

    tests_require=[
        'pytest',
    ],

    entry_points={
        'console_scripts': [],
    },
)
