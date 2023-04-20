#! /usr/bin/env python
import rospy
from std_msgs.msg import String

""" 
    订阅者实现流程：
        1.导包
        2.初始化ros节点
        3.创建订阅者对象
        4.回调函数处理数据
        5.spin()
"""
def domsg(msg):
    rospy.loginfo("我订阅的数据是：%s",msg.data)

if __name__=="__main__":
        # 2.初始化ros节点
    rospy.init_node("huahua")
        # 3.创建订阅者对象
    sub=rospy.Subscriber("fang",String,domsg,queue_size=10)
        # 4.回调函数处理数据
        # 5.spin()
    rospy.spin()
    pass