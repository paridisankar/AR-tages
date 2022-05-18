# AR-tages

I have use ros noetic for creating the Ar-tages 

for that i have used ar_track_alvar-noetic-devel-san 

Use https://github.com/ros-perception/ar_track_alvar.git

~$ mkdir catkin_ws/src

~$ cd catkin_ws

~$ catkin_make 

~$ git clone https://github.com/ros-perception/ar_track_alvar.git

~$ catkin_make

usb_cam Build Status
A ROS Driver for V4L USB Cameras

This package is based off of V4L devices specifically instead of just UVC.

For full documentation, see the ROS wiki.

Doxygen files can be found on the ROS wiki.
License

usb_cam is released with a BSD license. For full terms and conditions, see the LICENSE file.
Authors

See the AUTHORS file for a full list of contributors.

And for setting the turtlebot enveroment i have used

cd catkin_ws cd src git clone https://github.com/madhu-korada/AR_tag_detection_with_turtlebot3_gazebo.git

cd .. catkin_make

for the ar_turtlebot3 enveroment

and

$ export TURTLEBOT3_MODEL=burger

$ source devel/setup.bash

$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

$ rqt_image_view

$ rosed ar_track_alvar pr2_indiv_no_kinect.launch

$ roslaunch ar_track_alvar pr2_indiv_no_kinect.launch

$ rviz





