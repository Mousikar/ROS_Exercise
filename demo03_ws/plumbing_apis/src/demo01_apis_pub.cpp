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
    /*
        作用：ROS初始化参数

        参数：
            1.argc      ————封装实参个数（n+1文件自身）
            2.argv      ————封装参数的数组
            3.names     ————为节点命名（唯一性）
            4.options   ——节点启动选项

            返回值：void

        使用： 
            1.argc与argv的使用
                如果按照ros 中的特定格式传入实参，ros可以加以使用，比如用来设置全局参数，给节点重命名
            2.option的使用
                节点名称需要保证唯一，会导致一个问题：同一个节点不能重复启动
                当有同名的节点启动时，之前的节点会被关闭
                需求：特定场景下，需要一个节点多次使用，且能正常运行
                解决：设置启动项，ros::init_options::AnonymousName
                    当创建ros节点时，会在用户自定义的节点名称后缀随机数，从而避免重名问题
     */
    ros::init(argc,argv,"ergouzi",ros::init_options::AnonymousName);
    //3.创建节点句柄
    ros::NodeHandle nh;
    //4.创建发布者对象
    /*
        作用：创建发布者对象
        模板：被发布的消息的类型
        语法：
            1.话题名称
            2.队列长度
            3.latch（可选）如果设置为true，保存发布者的最后一条消息，并且新的订阅对象连接到发布方时，发布对象会将这条消息发布给订阅者
        使用： 
            latch设置为true的作用？
                以静态地图发布为例，方案1：可以使用固定频率发布地图数据，但是效率低；方案2：可以将地图发布对象的latch设置为true，每当订阅者连接时，只发布一次数据
     */
    ros::Publisher pub=nh.advertise<std_msgs::String>("fang",10,true);//话题是fang，队列长度是10
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
        if(count>=50){
            ros::shutdown();
        }
        count++;

        //实现字符串的拼接
        std::stringstream ss;
        ss<<"hello-------"<<count;
        //msg.data="hello";
        msg.data=ss.str();
        // if(count<=10){
        // pub.publish(msg);
        // //添加日志
        // ROS_INFO("发布的数据是：%s",ss.str().c_str());//ros中的字符
        // }
        rate.sleep();
        ros::spinOnce();//官方建议，处理循环中的回调函数
        ROS_INFO("一轮回调执行完毕");
    }
    return 0;
}
