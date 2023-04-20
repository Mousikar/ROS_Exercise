#! /usr/bin/env python

import rospy

""" 演示参数的删除：
    delete_param
 """
if __name__=="__main__":
    # 初始化ros节点
    rospy.init_node("param_set_p")
    try:
    # 删除参数
        rospy.delete_param("radius_p")
    except Exception as e:
        rospy.loginfo("no exist!")