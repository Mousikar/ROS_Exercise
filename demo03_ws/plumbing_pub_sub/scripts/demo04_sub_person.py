#! /usr/bin/env python
import rospy 
from plumbing_pub_sub.msg import Person
""" 
订阅方：订阅人的消息数据
    1.导包
    2.初始化ros节点
    3.创建订阅者对象
    4.处理订阅到的数据，回调函数
    5.spin()
 """
def doPerson(p):
    rospy.loginfo("订阅到的数据：%s,%d,%.2f",p.name,p.age,p.height)

if __name__=="__main__":
    # 2.初始化ros节点
    rospy.init_node("daye")
    # 3.创建订阅者对象
    sub=rospy.Subscriber("jiaoshetou",Person,doPerson)
    # 4.处理订阅到的数据，回调函数
    # 5.spin()
    rospy.spin()