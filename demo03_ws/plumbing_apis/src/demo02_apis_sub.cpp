#include "ros/ros.h"
#include "std_msgs/String.h"//接收到的数据

/*
    订阅方实现：
        1.包含头文件
            ros中的文本类型   对应  std_msgs/String.h
        2.初始化ROS 节点
        3.创建节点句柄
        4.创建订阅者对象
        5.编写订阅到的数据
        6.spin()函数
*/

void doMsg(const std_msgs::String::ConstPtr &msg){
    //通过msg来获取并操作订阅到的数据
    ROS_INFO("翠花订阅的数据：%s",msg->data.c_str());
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    //2.初始化ROS 节点
    ros::init(argc,argv,"cuihua");
    //3.创建节点句柄
    ros::NodeHandle nh;
    //4.创建订阅者对象
    ros::Subscriber sub=nh.subscribe("fang",10,doMsg);//泛行类型可以自己推导
    //5.编写订阅到的数据

    ros::spin();//字面意思：回头，调用回调函数，如果没有这个函数，可能订阅不到，消息打印不出来
    ROS_INFO("一轮回调执行完毕");
    return 0;
}
