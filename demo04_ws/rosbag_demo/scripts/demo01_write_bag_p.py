#! /usr/bin/env python
import rospy
import rosbag
from std_msgs.msg import String

""" 
    需求：使用rosbag向磁盘文件写出数据（话题+消息）
    流程：
        1. 导包；
        2. 初始化；
        3. 创建rosbag对象；
        4. 写数据；
        6. 关闭文件流
 """

if __name__ == "__main__":
    #初始化节点 
    rospy.init_node("w_bag_p")

    # 创建 rosbag 对象
    bag = rosbag.Bag("test_p.bag",'w')#w是write

    # 写数据
    s = String()
    s.data= "hahahaha"

    bag.write("chatter",s)
    bag.write("chatter",s)
    bag.write("chatter",s)
    bag.write("chatter",s)

    bag.write("chatter",s)
    bag.write("chatter",s)
    bag.write("chatter",s)
    bag.write("chatter",s)
    # 关闭流
    bag.close()
