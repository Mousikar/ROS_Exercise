#! usr/bin/env python
import string
import rospy
from std_msgs.msg import String     #发布的消息的类型

'''
    使用python实现消息发布
        1.导包
        2.初始化ros节点
        3.创建发布者对象
        4.编写发布者逻辑并发布数据
    
'''

def cb():
    rospy.loginfo("节点正在关闭")

if __name__=="__main__":
    # 2.初始化ros节点
    """ 作用：ROS初始化

    参数：
        name：设置节点名称
        argv=None，封装节点调用时传递的参数
        anonymous=False，可以为节点名称生成随机后缀，可以解决重名问题
    使用：
        1.argv使用
        可以按照ros中指定的语法格式传参，ros可以解析并加以使用
        2.anonymous使用
        可以设置值为True，节点名称后缀随机数，避免重名问题
     """
    rospy.init_node("saidai",anonymous=True)       #传入节点名称
    # 3.创建发布者对象
    """
        内容：latch
            bool值，默认false
        作用：
            如果设置为True，可以将发布的最后一项数据保存，且当新的订阅对象连接时，会将该数据发送给订阅者
        使用： 
            latch=True
    """
    # pub=rospy.Publisher("che",String,queue_size=10,latch=True)
    pub=rospy.Publisher("che",String,queue_size=10)
    # 4.编写发布者逻辑并发布数据
    #创建数据
    msg=String()
    #指定发布频率
    rate=rospy.Rate(1)
    #设置计数器
    count=0
    #使用循环发布数据
    rospy.sleep(3)
    while not rospy.is_shutdown():
        count+=1
        if count<=10:
            msg.data="hello"+str(count)
    #发布数据
            pub.publish(msg)
            rospy.loginfo("发布的数据是：%s",msg.data)
        else:
            # 关闭节点
            rospy.on_shutdown(cb)
            rospy.signal_shutdown("关闭节点")
        rate.sleep()
    