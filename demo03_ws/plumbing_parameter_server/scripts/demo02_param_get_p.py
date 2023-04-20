#! /usr/bin/env python

import rospy

""" 
    参数服务器操作之查询_Python实现:    
        get_param(键,默认值)
            当键存在时，返回对应的值，如果不存在返回默认值 rpc协议
        get_param_cached
            和get_param使用一致，返回对应的值，只是效率高 从本地缓存取得数据
        get_param_names
            获得所有参数建的组合
        has_param
            判断是否包含某个键
        search_param
            查找某个参数的建，并返回完整的键名
"""

if __name__=="__main__":
    # 初始化ros节点
    rospy.init_node("param_set_p")
    # 1.get_param
    radius=rospy.get_param("radius_p",0.5)
    rospy.loginfo("radius=%.2f",radius)
    radius1=rospy.get_param("radius1_P",0.5)
    rospy.loginfo("radius1=%.2f",radius1)

    # 2.get_param_cached
    radius=rospy.get_param_cached("radius_p",0.5)
    rospy.loginfo("radius=%.2f",radius)
    radius1=rospy.get_param_cached("radius1_P",0.5)
    rospy.loginfo("radius1=%.2f",radius1)

    # 3.get_param_names
    names=rospy.get_param_names()
    for name in names:
        rospy.loginfo("name=%s",name)

    # 4.has_param
    flag1=rospy.has_param("radius_p")
    if flag1:
        rospy.loginfo("exist!")
    else:
        rospy.loginfo("no")
    flag2=rospy.has_param("raadius_p")
    if flag2:
        rospy.loginfo("exist!")
    else:
        rospy.loginfo("no")

    # 5.search_param
    key=rospy.search_param("radius_p")
    rospy.loginfo("key=%s",key)