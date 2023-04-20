#include "ros/ros.h"
/* 需求：修改参数服务器中turtlesim背景色相关的参数
    1.初始化ros节点
    2.不一定需要创建节点句柄（和后续API有关)
    3.修改参数
    如果调用ros::param不需要创建节点句柄
*/

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"change_clolor");
    // 方法一
    // ros::param::set("/turtlesim/background_r",0);
    // ros::param::set("/turtlesim/background_g",0);
    // ros::param::set("/turtlesim/background_b",0);
    // 方法二
    // ros::NodeHandle nh("turtlesim");
    // nh.setParam("background_r",250);
    // nh.setParam("background_g",250);
    // nh.setParam("background_b",250);
    // 方法三
    ros::NodeHandle nh;
    nh.setParam("/turtlesim/background_r",150);
    nh.setParam("/turtlesim/background_g",250);
    nh.setParam("/turtlesim/background_b",250);

    return 0;
}
