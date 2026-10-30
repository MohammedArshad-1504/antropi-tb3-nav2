# TurtleBot3 Autonomous Navigation with ROS 2 Nav2

Autonomous navigation of a TurtleBot3 Waffle in a custom Gazebo Sim environment using the ROS 2 Navigation2 (Nav2) stack on ROS 2 Jazzy.

Built for the **Robotics Software Intern assignment at Antropi Robotics**.

> **Demo video:** [Watch the autonomous navigation demo](https://drive.google.com/file/d/1mE8lElqcWw7Jmwgwrmn7jkd5z81pPbt0/view?usp=drivesdk)

---

## Overview

This project demonstrates autonomous navigation of a TurtleBot3 Waffle in a custom Gazebo Sim environment.

The robot starts in a large hall with four corner rooms and scattered obstacles. A map of the environment was created using SLAM Toolbox, and the robot localizes on the saved map using AMCL. Nav2 then plans a global path to a goal selected in RViz and follows it using a local controller while avoiding obstacles detected by the simulated LiDAR.

No custom navigation algorithm was implemented. Planning, control, localization, and obstacle avoidance are handled using standard ROS 2 Nav2 components.

## Tested Environment

| Component | Version |
|---|---|
| OS | Ubuntu 24.04 |
| ROS 2 | Jazzy |
| Simulator | Gazebo Sim 8.11.0 |
| Robot | TurtleBot3 Waffle |
| Navigation | Nav2 (AMCL, NavFn, DWB) |

## Features

- Custom Gazebo world with a large hall, four corner rooms, doorways, and obstacles
- TurtleBot3 Waffle with simulated LiDAR and odometry
- Map generated using SLAM Toolbox and saved as `.pgm` / `.yaml`
- AMCL localization on the saved map
- Nav2 global and local costmaps
- NavFn global path planning
- DWB local control
- Autonomous goal navigation with obstacle avoidance
- Saved RViz configuration
- Dedicated launch files for simulation, Nav2 bringup, and RViz

## System Architecture

```text
                         Gazebo Sim
                             │
                    ┌────────┴────────┐
                    │                 │
                 LiDAR             Odometry
                (/scan)            (/odom)
                    │                 │
                    └────────┬────────┘
                             │
                            TF2
                             │
                     AMCL Localization
                             │
                  ┌──────────┴──────────┐
                  │                     │
             Global Costmap        Local Costmap
                  │                     │
             NavFn Planner          DWB Controller
                  │                     │
                  └──────────┬──────────┘
                             │
                          /cmd_vel
                             │
                      TurtleBot3 Waffle
```

## Repository Structure

```text
antropi-tb3-nav2/
└── src/
    └── antropi_tb3_nav/
        ├── antropi_tb3_nav/
        │   └── __init__.py
        ├── config/
        │   └── nav2_params.yaml
        ├── launch/
        │   ├── sim.launch.py
        │   ├── bringup.launch.py
        │   └── rviz.launch.py
        ├── maps/
        │   ├── antropi_map.pgm
        │   └── antropi_map.yaml
        ├── rviz/
        │   └── antropi_nav.rviz
        ├── scripts/
        │   └── generate_world.py
        ├── test/
        ├── worlds/
        │   └── antropi_world.sdf
        ├── package.xml
        ├── resource/
        │   └── antropi_tb3_nav
        ├── setup.cfg
        └── setup.py
```

## Prerequisites

The project was developed and tested with:

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Sim 8.11.0
- TurtleBot3 packages
- Navigation2
- SLAM Toolbox
- `ros_gz`

Install the main dependencies with:

```bash
sudo apt update
sudo apt install -y   ros-jazzy-navigation2   ros-jazzy-nav2-bringup   ros-jazzy-slam-toolbox   ros-jazzy-ros-gz   ros-jazzy-turtlebot3   ros-jazzy-turtlebot3-msgs   ros-jazzy-turtlebot3-description   ros-jazzy-turtlebot3-gazebo
```

## Installation

Clone the repository:

```bash
cd ~
git clone https://github.com/MohammedArshad-1504/antropi-tb3-nav2.git
cd antropi-tb3-nav2
```

Build the workspace:

```bash
colcon build --symlink-install
```

Source ROS 2 and the workspace:

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
```

Set the TurtleBot3 model:

```bash
export TURTLEBOT3_MODEL=waffle
```

## Running the Simulation

### Terminal 1 — Gazebo

```bash
cd ~/antropi-tb3-nav2
source /opt/ros/jazzy/setup.bash
source install/setup.bash
export TURTLEBOT3_MODEL=waffle

ros2 launch antropi_tb3_nav sim.launch.py
```

### Terminal 2 — Nav2

After Gazebo is running:

```bash
cd ~/antropi-tb3-nav2
source /opt/ros/jazzy/setup.bash
source install/setup.bash
export TURTLEBOT3_MODEL=waffle

ros2 launch antropi_tb3_nav bringup.launch.py
```

### Terminal 3 — RViz

```bash
cd ~/antropi-tb3-nav2
source /opt/ros/jazzy/setup.bash
source install/setup.bash

ros2 launch antropi_tb3_nav rviz.launch.py
```

## Sending a Navigation Goal

1. Open RViz and verify that the robot, LiDAR scan, and map are aligned.
2. If necessary, use **2D Pose Estimate** to initialize/correct the robot pose.
3. Select **Nav2 Goal** / **2D Goal Pose**.
4. Click a destination on the map.
5. Nav2 computes a global path and commands the robot toward the goal while avoiding obstacles.

A useful demonstration route is from the open central area into one of the corner rooms, requiring the robot to navigate around obstacles and through a doorway.

## Custom Environment

The custom Gazebo world is defined in:

```text
worlds/antropi_world.sdf
```

The environment contains:

- Outer boundary walls
- Four corner rooms
- One doorway for each room
- Obstacles in the central area and rooms
- Static Gazebo environment models

The world-generation script is:

```text
scripts/generate_world.py
```

It can be used to regenerate the SDF during development:

```bash
python3 src/antropi_tb3_nav/scripts/generate_world.py
```

> Running the script overwrites `worlds/antropi_world.sdf`.

## Mapping

The navigation map was created during development using SLAM Toolbox and TurtleBot3 teleoperation.

A typical mapping workflow is:

```bash
# Terminal 1 — simulation
ros2 launch antropi_tb3_nav sim.launch.py
```

```bash
# Terminal 2 — SLAM Toolbox
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

```bash
# Terminal 3 — teleoperation
ros2 run turtlebot3_teleop teleop_keyboard
```

After completing the mapping run:

```bash
ros2 run nav2_map_server map_saver_cli   -f src/antropi_tb3_nav/maps/antropi_map
```

The resulting map files are stored in:

```text
maps/
├── antropi_map.pgm
└── antropi_map.yaml
```

## Nav2 Configuration

The main Nav2 configuration is stored in:

```text
config/nav2_params.yaml
```

| Component | Configuration |
|---|---|
| Localization | AMCL |
| Global planner | NavFn |
| Local controller | DWB |
| Global costmap | Static map + obstacle + inflation layers |
| Local costmap | Rolling window + obstacle/voxel + inflation layers |

### Navigation flow

1. Gazebo provides simulated sensor and odometry data.
2. LiDAR publishes `/scan`.
3. Odometry publishes `/odom`.
4. TF2 maintains the robot coordinate-frame relationships.
5. AMCL estimates the robot pose on the saved map.
6. Nav2 builds the global and local costmaps.
7. NavFn calculates a global path.
8. DWB generates velocity commands.
9. `/cmd_vel` drives the simulated TurtleBot3.

## Challenges

### Map and simulation coordinate alignment

The Gazebo world and saved navigation map do not need to share identical coordinates. Correct AMCL initialization is therefore important so that the LiDAR scan aligns with the map.

### Simulation time

ROS 2 nodes interacting with Gazebo must use simulation time consistently. Incorrect time configuration can cause TF and visualization problems.

### Costmap visualization

During development, costmap visualization in RViz required additional checking of topics, lifecycle states, subscriptions, and QoS. Navigation and obstacle avoidance were still functional.

### World design

Room entrances and obstacle gaps had to provide enough clearance for the TurtleBot3 and Nav2 costmap inflation. The world-generation script made it easier to adjust the environment geometry.

## What I Learned

- ROS 2 package and launch-file structure
- Gazebo Sim world creation using SDF
- TurtleBot3 simulation
- ROS 2 TF2 coordinate frames
- AMCL localization
- Nav2 architecture
- Global and local costmaps
- NavFn global planning
- DWB local control
- LiDAR-based obstacle detection
- SLAM Toolbox mapping
- RViz-based localization and goal setting
- Debugging ROS 2 systems using topics, lifecycle states, TF, and QoS
- Git and GitHub project management

## Future Improvements

- Compare additional Nav2 planners and controllers
- Tune AMCL and costmap parameters further
- Add dynamic obstacles
- Add waypoint-following missions across multiple rooms
- Test larger environments
- Explore multi-robot navigation

## Demo

**Demo video:** [Watch the autonomous navigation demo](https://drive.google.com/file/d/1mE8lElqcWw7Jmwgwrmn7jkd5z81pPbt0/view?usp=drivesdk)

The demonstration shows the TurtleBot3 navigating autonomously through the custom environment while using Nav2 for planning, control, localization, and obstacle avoidance.

## Author

**Mohammed Arshad S.**

B.E. Mechatronics Engineering  
Robotics / ROS 2 / Embedded Systems
