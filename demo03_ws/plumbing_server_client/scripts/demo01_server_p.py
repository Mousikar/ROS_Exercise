#! ./usr/bin/env python

import logging
import rospy
from plumbing_server_client.srv import AddInts,AddIntsResponse,AddIntsRequest
""" 服务器：解析客户端请求，产生响应
    1.导包
    2.初始化ros节点
    3.创建服务端对象
    4.处理逻辑（回调函数）
    5.spin()
"""
# 参数：封装了请求数据
# 返回值：响应数据
def doNums(request):
    # 1.解析提交的整数
    num1=request.num1
    num2=request.num2
    # 2.求和
    sum=num1+num2
    # 3.将结果封装进响应
    respose=AddIntsResponse()
    respose.sum=sum
    rospy.loginfo("服务器解析的数据是num1=%d,num2=%d,响应的结果sum=%d",num1,num2,sum)
    return respose

if __name__=="__main__":
    # 2.初始化ros节点
    rospy.init_node("heiShui")
    # 3.创建服务端对象
    server=rospy.Service("AddInts",AddInts,doNums)
    rospy.loginfo("服务器启动")
    # 4.处理逻辑（回调函数）
    # 5.spin()
    rospy.spin()