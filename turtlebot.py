#!/usr/bin/env python
import rospy
from geomentry_msgs.msg import Twist, Point
from ar_track_alvar_msgs.msg import AlvarMarkers 

Turtlebot = Point()

def getTurtlebot(msg):
    global turtlebot
    if len(msg.markers) == 1:
        Turtlebot = msg.markers[0].pose.pose.position
    else:
        Turtlebot = Point()
        
rospy.init_node ("Turtlebot_navigation")


markers =rospy.Subscriber ("/ar_pose_marker" , AlvarMarkers, getturTurtlebot)
move = rospy.Publisher("/aiboERS7/cmd_vel" ,Twist, queue_size=1)

r = rospy.Rate(1)

speed = Twist()

while not rospy.is_shutdown():

    speed.linear.x = Turtlebot.y / 10
    speed.anguler.z = Turtlebot.x / 2
    
    print speed 
    
    move.publish(speed)
    
    f.sleep()
