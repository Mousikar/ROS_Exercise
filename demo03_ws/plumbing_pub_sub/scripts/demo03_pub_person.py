#! /usr/bin/env python

from ast import While
import rospy
from plumbing_pub_sub.msg import Person
""" 
发布方：发布人的消息数据
    1.导包
    2.初始化ros节点
    3.创建发布者对象
    4.组织发布逻辑，并发布数据
 """
if __name__=="__main__":
    pass

    # 2.初始化ros节点
    rospy.init_node("dama")
    # 3.创建发布者对象
    pub=rospy.Publisher("jiaoshetou",Person,queue_size=10)
    # 4.组织发布逻辑，并发布数据
    #4-1创建Person数据
    p=Person()
    p.name="欧特曼"
    p.age=8
    p.height=1.85
    #4-2创建Rate对象
    rate=rospy.Rate(1)
    #循环发布数据
    while not rospy.is_shutdown():
        pub.publish(p)
        rate.sleep()
        rospy.loginfo("发布的数据是：%s,%d,%.2f",p.name,p.age,p.height)