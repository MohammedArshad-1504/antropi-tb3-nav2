<?xml version="1.0" ?>
<sdf version="1.9">

  <world name="antropi_world">

    <!-- ========================================================= -->
    <!-- PHYSICS                                                   -->
    <!-- ========================================================= -->

    <physics name="1ms" type="ode">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
    </physics>

    <gravity>0 0 -9.81</gravity>

    <!-- ========================================================= -->
    <!-- SCENE                                                     -->
    <!-- ========================================================= -->

    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>true</shadows>
    </scene>

    <!-- ========================================================= -->
    <!-- SUN                                                       -->
    <!-- ========================================================= -->

    <light name="sun"
           type="directional">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <direction>-0.5 0.1 -0.9</direction>
    </light>


    <!-- ========================================================= -->
    <!-- FLOOR                                                     -->
    <!-- ========================================================= -->

    <model name="floor">

      <static>true</static>

      <link name="floor_link">

        <collision name="collision">

          <geometry>
            <box>
              <size>12.0 9.0 0.1</size>
            </box>
          </geometry>

        </collision>

        <visual name="visual">

          <geometry>
            <box>
              <size>12.0 9.0 0.1</size>
            </box>
          </geometry>

          <material>
            <ambient>0.75 0.75 0.75 1</ambient>
            <diffuse>0.75 0.75 0.75 1</diffuse>
          </material>

        </visual>

      </link>

      <pose>0 0 -0.05 0 0 0</pose>

    </model>


    <!-- ========================================================= -->
    <!-- OUTER WALLS                                               -->
    <!-- ========================================================= -->

    <model name="outer_walls">

      <static>true</static>

      <!-- ------------------------------------------------------- -->
      <!-- LEFT OUTER WALL                                         -->
      <!-- ------------------------------------------------------- -->

      <link name="left_wall">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 9.0 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 9.0 1.0</size>
            </box>
          </geometry>

          <material>
            <ambient>0.55 0.55 0.55 1</ambient>
            <diffuse>0.55 0.55 0.55 1</diffuse>
          </material>
        </visual>

        <pose>-5.925 0 0.5 0 0 0</pose>

      </link>


      <!-- ------------------------------------------------------- -->
      <!-- RIGHT OUTER WALL                                        -->
      <!-- ------------------------------------------------------- -->

      <link name="right_wall">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 9.0 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 9.0 1.0</size>
            </box>
          </geometry>

          <material>
            <ambient>0.55 0.55 0.55 1</ambient>
            <diffuse>0.55 0.55 0.55 1</diffuse>
          </material>
        </visual>

        <pose>5.925 0 0.5 0 0 0</pose>

      </link>


      <!-- ------------------------------------------------------- -->
      <!-- TOP OUTER WALL                                          -->
      <!-- ------------------------------------------------------- -->

      <link name="top_wall">

        <collision name="collision">
          <geometry>
            <box>
              <size>12.0 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>12.0 0.15 1.0</size>
            </box>
          </geometry>

          <material>
            <ambient>0.55 0.55 0.55 1</ambient>
            <diffuse>0.55 0.55 0.55 1</diffuse>
          </material>
        </visual>

        <pose>0 4.425 0.5 0 0 0</pose>

      </link>


      <!-- ------------------------------------------------------- -->
      <!-- BOTTOM OUTER WALL                                       -->
      <!-- ------------------------------------------------------- -->

      <link name="bottom_wall">

        <collision name="collision">
          <geometry>
            <box>
              <size>12.0 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>12.0 0.15 1.0</size>
            </box>
          </geometry>

          <material>
            <ambient>0.55 0.55 0.55 1</ambient>
            <diffuse>0.55 0.55 0.55 1</diffuse>
          </material>
        </visual>

        <pose>0 -4.425 0.5 0 0 0</pose>

      </link>

    </model>


    <!-- ========================================================= -->
    <!-- ROOM WALLS                                                -->
    <!-- ========================================================= -->

    <model name="room_walls">

      <static>true</static>


      <!-- ======================================================= -->
      <!-- TOP LEFT ROOM                                           -->
      <!-- Room approximately 3.4m x 2.8m                         -->
      <!-- Entrance on right side                                  -->
      <!-- ======================================================= -->

      <!-- Left wall is already provided by outer wall -->

      <link name="tl_top">

        <collision name="collision">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>-4.15 4.0 0.5 0 0 0</pose>

      </link>


      <link name="tl_bottom">

        <collision name="collision">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <!-- Leaves approximately 1.0m entrance -->
        <pose>-4.725 1.5 0.5 0 0 0</pose>

      </link>


      <link name="tl_right">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>-2.45 3.225 0.5 0 0 0</pose>

      </link>


      <!-- ======================================================= -->
      <!-- TOP RIGHT ROOM                                          -->
      <!-- ======================================================= -->

      <link name="tr_top">

        <collision name="collision">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>4.15 4.0 0.5 0 0 0</pose>

      </link>


      <link name="tr_bottom">

        <collision name="collision">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>4.725 1.5 0.5 0 0 0</pose>

      </link>


      <link name="tr_left">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>2.45 3.225 0.5 0 0 0</pose>

      </link>


      <!-- ======================================================= -->
      <!-- BOTTOM LEFT ROOM                                        -->
      <!-- ======================================================= -->

      <link name="bl_bottom">

        <collision name="collision">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>-4.15 -4.0 0.5 0 0 0</pose>

      </link>


      <link name="bl_top">

        <collision name="collision">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>-4.725 -1.5 0.5 0 0 0</pose>

      </link>


      <link name="bl_right">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>-2.45 -3.225 0.5 0 0 0</pose>

      </link>


      <!-- ======================================================= -->
      <!-- BOTTOM RIGHT ROOM                                       -->
      <!-- ======================================================= -->

      <link name="br_bottom">

        <collision name="collision">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>3.5 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>4.15 -4.0 0.5 0 0 0</pose>

      </link>


      <link name="br_top">

        <collision name="collision">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>2.35 0.15 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>4.725 -1.5 0.5 0 0 0</pose>

      </link>


      <link name="br_left">

        <collision name="collision">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.15 1.55 1.0</size>
            </box>
          </geometry>
        </visual>

        <pose>2.45 -3.225 0.5 0 0 0</pose>

      </link>

    </model>


    <!-- ========================================================= -->
    <!-- NO GENERATED OBSTACLES                                   -->
    <!-- ========================================================= -->

    <!--
      Obstacles are intentionally NOT included here.

      We will place them manually in Gazebo after verifying
      that the room geometry and robot navigation are correct.
    -->


  </world>

</sdf>
