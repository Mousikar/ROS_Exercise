#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
/*
    发布方实现：
        1.包含头文件
            ros中的文本类型   对应  std_msgs/String.h
        2.初始化ROS 节点
        3.创建节点句柄
        4.创建发布者对象
        5.编写发布逻辑，并发布数据
*/

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");//中文
    //2.初始化ros节点
    ros::init(argc,argv,"ergouzi");
    //3.创建节点句柄
    ros::NodeHandle nh;
    //4.创建发布者对象
    ros::Publisher pub=nh.advertise<std_msgs::String>("fang",10);//话题是fang，队列长度是10
    //5.编写发布逻辑，并发布数据
    //要求以10Hz的频率发布数据，并且文本后添加编号
    //先创建被发布的消息
    std_msgs::String msg;
    //发布频率
    ros::Rate rate(1);
    //设置编号
    int count=0;
    //编写循环，循环中发布数据
    ros::Duration(3).sleep();//休眠三秒钟，先注册在发送
    while (ros::ok())//节点还正常运行
    {
        count++;

        //实现字符串的拼接
        std::stringstream ss;
        ss<<"hello-------"<<count;
        //msg.data="hello";
        msg.data=ss.str();

        pub.publish(msg);
        //添加日志
        ROS_INFO("发布的数据是：%s",ss.str().c_str());//ros中的字符

        rate.sleep();
        ros::spinOnce();//官方建议，处理循环中的回调函数
    }
    return 0;
}
