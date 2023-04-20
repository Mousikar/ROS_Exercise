#! /usr/bin/env python
""" 需求：修改参数服务器中turtlesim背景色相关的参数
    1.初始化ros节点
    2.修改参数
    如果调用ros::param不需要创建节点句柄
"""
import rospy
if __name__=="__main__":
    rospy.init_node("change_colour_p")
    rospy.set_param("/turtlesim/background_r",100)
    rospy.set_param("/turtlesim/background_g",100)
    rospy.set_param("/turtlesim/background_b",200)