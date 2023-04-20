#! /usr/bin/env python
""" 
    需求1：演示时间相关操作（获取当前时间+设置指定时间）
    实现：
        2.获取当前时刻
        3.设置
    需求2：程序执行中停顿5秒
    实现：
        1.创建持续时间对象；
        2.休眠
    需求3：已知程序开始运行的时间，和程序运行的时间，求程序运行结束的时间
    实现：
        1.获取开始执行的时间
        2.模拟运行时间
        3.计算结束时间=开始+持续时间
    注意：
        1.时刻与持续时间可以执行加减
        2.持续时间之间也可以执行加减
        3.时刻之间值可以相见，不可以相加
    需求4：每隔一秒钟，在控制台输出一段文本
    实现：
        策略1：ros::Rate()
        策略2：定时器
    注意：
        创建：nh.createTimer()
        参数1：时间间隔
        参数2：回调函数（时间时间TimerEvent）
        参数3：是否只执行一次
        参数4：是否自动启动（当设置为false，需要手动调用timer.start()）

        定时器启动后：ros::spin()
"""
import rospy

def doMsg(event):
    rospy.loginfo("---------------")
    rospy.loginfo("调用回调函数的时刻：%.2f",event.current_real.to_sec())


if __name__=="__main__":
    # 需求1：演示时间相关操作（获取当前时间+设置指定时间）
    rospy.init_node("hello_time_p")
    # 实现：
    #     2.获取当前时刻
    right_now=rospy.Time.now()#获取当前时刻（1.调用被执行的那一刻2.1970年1月1日00：00：00）并封装成对象
    rospy.loginfo("当前时刻：%.2f",right_now.to_sec())
    rospy.loginfo("当前时刻：%d",right_now.secs)
    #     3.设置指定
    time1=rospy.Time(100)#将时间封装成Time对象1970年1月1日00：00：00）并封装成对象
    time2=rospy.Time(100,312345678)
    rospy.loginfo("当前时刻：%d",time1.to_sec())
    rospy.loginfo("当前时刻：%.2f",time2.to_sec())
    # 从某个时间值获取时间对象
    time3=rospy.Time.from_sec(210.12)
    rospy.loginfo("当前时刻：%d",time3.to_sec())

    # 需求2：程序执行中停顿5秒
    rospy.loginfo("休眠前")
    # 实现：
    #     1.创建持续时间对象；
    du=rospy.Duration(3)
    #     2.休眠
    rospy.sleep(du)
    rospy.loginfo("休眠后")

    # 需求3：已知程序开始运行的时间，和程序运行的时间，求程序运行结束的时间
    # 1.获取时刻
    t1=rospy.Time.now()
    rospy.loginfo("获取时刻%.2f",t1.to_sec())
    # 2.持续时间
    du1=rospy.Duration(2)
    # 3.结束时间
    t2=t1+du1
    rospy.loginfo("结束时间%.2f",t2.to_sec())

    du2=du+du1
    rospy.loginfo("相加%.2f",du2.to_sec())
    # 需求4：每隔一秒钟，在控制台输出一段文本
    """
    Constructor.
    @param period: desired period between callbacks
    @type  period: rospy.Duration
    @param callback: callback to be called
    @type  callback: function taking rospy.TimerEvent
    @param oneshot: if True, fire only once, otherwise fire continuously until shutdown is called [default: False]
    @type  oneshot: bool
    @param reset: if True, timer is reset when rostime moved backward. [default: False]
    @type  reset: bool
    """
    # timer=rospy.Timer(rospy.Duration(2),doMsg,True)
    timer=rospy.Timer(rospy.Duration(2),doMsg)
    rospy.spin()