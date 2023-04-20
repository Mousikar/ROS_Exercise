#! /usr/bin/env python

import rospy

if __name__=="__main__":
    rospy.init_node("hello_log")
    rospy.logdebug("debug")
    rospy.loginfo("loginfo")
    rospy.logwarn("warn")
    rospy.logerr("error")
    rospy.logfatal("fatal")