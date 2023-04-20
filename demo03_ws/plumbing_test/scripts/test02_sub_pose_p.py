#! /usr/bin/env python

import rospy
from turtlesim.msg import Pose
""" 订阅并输出乌龟位姿信息
1.导包
2.初始化ros节点
3.创建订阅对象
4.使用回调函数处理订阅到的消息
5.spin()
 """
def doPose(pose):
    rospy.loginfo("P->乌龟位姿信息：坐标:(%.2f,%.2f),朝向:%.2f,线速度：%.2f角速度：%.2f",pose.x,pose.y,pose.theta,pose.linear_velocity,pose.angular_velocity)

if __name__=="__main__":
    rospy.init_node("sub_pose_p")
    sub=rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    rospy.spin()
