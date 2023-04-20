#! /usr/bin/env python

# 现象：当不配置CMAKEList。txt执行python文件时抛出异常
# /opt/ros/noetic/bin/rosrun: 行 150: /home/rosnoetic/demo02_ws/src/hello_vscode/scripts/hello_no_config.py: 成功
# 原因：当前noetic版本使用的是python3
# 解决：
#   1.直接声明解释器声明成python3（不建议）
#   2.通过软连接将python连接到python3上(建议)
#       sudo ln -s /usr/bin/python3 /usr/bin/python

#导包
import rospy
#入口
if __name__=="__main__":
    #初始化ros节点
    rospy.init_node("hello_p")

    #输出日志
    rospy.loginfo("hello vscode!这是python！22222222222222222222222222222222222222222222")