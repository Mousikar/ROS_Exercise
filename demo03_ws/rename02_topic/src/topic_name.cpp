#include "ros/ros.h"
#include "std_msgs/String.h"

/*
    需求：演示不同类型的话题名称配置
        设置话题名称与命名空间
*/

int main(int argc, char  *argv[])
{
    ros::init(argc,argv,"hello");
    // ros::NodeHandle nh;
    // 核心：设置不同类型的话题
    // 1.全局-----话题名称需要以斜杠/开头（也可以设置自己的命名空间），这种情况下和节点的命名空间和名字没有关系
    // ros::Publisher pub=nh.advertise<std_msgs::String>("/chatter",1000);
    // ros::Publisher pub=nh.advertise<std_msgs::String>("/yyy/chatter",1000);

    // 2.相对-----非斜杠开头，相对于节点命名空间
    // ros::Publisher pub=nh.advertise<std_msgs::String>("chatter",1000);
    // ros::Publisher pub=nh.advertise<std_msgs::String>("yyy/chatter",1000);

    // 3.私有-----需要创建特定NodeHandle,但是全局的优先级更高
    ros::NodeHandle nh("~");
    // ros::Publisher pub=nh.advertise<std_msgs::String>("chatter",1000);
    ros::Publisher pub=nh.advertise<std_msgs::String>("yyy/chatter",1000);

    //注意：如果私有的NH创建的话题以/开头（全局话题），生成的话题是全局的非私有
    // 全局话题优先级更高 
    // ros::Publisher pub=nh.advertise<std_msgs::String>("/yyy/chatter",1000);

    while (ros::ok())
    {
        
    }
    
    
    return 0;
}
