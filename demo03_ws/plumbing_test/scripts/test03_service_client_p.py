#! /usr/bin/env python

import rospy
from turtlesim.srv import Spawn,SpawnRequest,SpawnResponse

""" 需求：是向服务器发送请求，生成一只新的乌龟
    话题：/spawn
    消息:turtlesim/Spawn
    1.导包
    2.初始化ros节点
    3.创建客户端对象
    4.组织数据并发送请求
    5.处理响应结果
"""
if __name__=="__main__":
    # 2.初始化ros节点
    rospy.init_node("service_call_p")
    # 3.创建客户端对象
    client=rospy.ServiceProxy("/spawn",Spawn)
    # 4.组织数据并发送请求
    # 4-1组织数据
    request=SpawnRequest()
    request.x=4.5
    request.y=2.0
    request.theta=-3
    request.name="turtle3"
    # 4-2判断服务器状态
    client.wait_for_service()
    # 4-3发送数据
    try:
        response=client.call(request)
        # 5.处理响应结果
        rospy.loginfo("生成乌龟的名字叫%s",response.name)
    except Exception as e:
        rospy.logerr("请求处理异常")