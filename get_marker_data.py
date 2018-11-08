#!/usr/bin/env python

import rospy
import roslib
import tf

from geometry_msgs.msg import PoseArray
from aruco_msgs.msg import MarkerArray


#Defining a class
class Marker_detect():

	def __init__(self):
		rospy.init_node('marker_detection',anonymous=False) # initializing a ros node with name marker_detection

		self.whycon_marker = {}	# Declaring dictionaries
		self.aruco_marker = {}

		rospy.Subscriber('/whycon/poses',PoseArray,self.whycon_data)	# Subscribing to topic
		rospy.Subscriber('/aruco_marker_publisher/markers',MarkerArray,self.aruco_data)	# Subscribing to topic
		


	# Callback for /whycon/poses
	def whycon_data(self,msg):
            rospy.loginfo(WhyCon_marker ,self.whycon_data)


	# Callback for /aruco_marker_publisher/markers
	def aruco_data(self,msg):
	    rospy.loginfo(ArUco_marker ,self.aruco_data)	


		# Printing the detected markers on terminal
		print "\n"
		print "WhyCon_marker",self.whycon_marker
		print "ArUco_marker",self.aruco_marker




if __name__=="__main__":

	marker = Marker_detect()
        marker.__init__();
	
	while not rospy.is_shutdown():
		rospy.spin()
