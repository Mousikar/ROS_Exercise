#include "ros/ros.h"
#include "rosbag/bag.h"
#include "std_msgs/String.h"
/* 
    需求：使用rosbag向磁盘文件写出数据（话题+消息）
    流程：
        1. 导包；
        2. 初始化；
        3. 创建rosbag对象；
        4. 写数据；
        6. 关闭文件流
 */
int main(int argc, char *argv[])
{
    ros::init(argc,argv,"bag_write");
    ros::NodeHandle nh;
    //创建bag对象
    rosbag::Bag bag;
    //打开文件流
    bag.open("test.bag",rosbag::BagMode::Write);
    //写
    std_msgs::String msg;
    msg.data = "hello world";
    /* 
        参数1：话题
        参数2：时间戳
        参数3：消息
     */
    bag.write("/chatter",ros::Time::now(),msg);
    bag.write("/chatter",ros::Time::now(),msg);
    bag.write("/chatter",ros::Time::now(),msg);
    bag.write("/chatter",ros::Time::now(),msg);
    //关闭
    bag.close();

    return 0;
}
