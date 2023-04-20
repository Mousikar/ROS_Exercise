#! /usr/bin/env python
from ast import Expression
from email import header
from logging import exception
import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs

""" 
    订阅方：订阅坐标变换消息，传入被转换的坐标点，调用转换算法
    流程：
        1.导包
        2.初始化
        3.创建订阅对象
        4.组织被转换的坐标点
        5.转换逻辑实现，调用tf封装的算法
        6.输出结果
 """
if __name__=="__main__":
    # 2.初始化
    rospy.init_node("static_sub_p")
    # 3.创建订阅对象
    # 3-1创建缓存对象
    buffer=tf2_ros.Buffer()
    # 3-2创建订阅对象（将缓存传入）
    sub=tf2_ros.TransformListener(buffer)
    # 4.组织被转换的坐标点
    ps=tf2_geometry_msgs.PointStamped()
    ps.header.stamp=rospy.Time.now()
    ps.header.frame_id="laser"
    ps.point.x=2.0
    ps.point.y=3.0
    ps.point.z=5.0
    # 5.转换逻辑实现，调用tf封装的算法
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # 转换实现
            """
                参数1：被转换的坐标点
                参数2：目标坐标系
                返回值：转换后的坐标点

                ps:
                问题：抛出异常 base_link不存在
                原因：转换函数调用时，可能还没有订阅到坐标系的相对信息
                解决：try捕获异常，并处理 
             """
            ps_out=buffer.transform(ps,"base_link")
            # 6.输出结果
            rospy.loginfo("转换后的坐标：(%.2f,%.2f,%.2f),参考的坐标系：%s",
                            ps_out.point.x,
                            ps_out.point.y,
                            ps_out.point.z,
                            ps_out.header.frame_id)
        except Exception as e:
            rospy.logwarn("错误提示：%s",e)
        rate.sleep()