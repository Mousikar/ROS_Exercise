#include "ros/ros.h"
#include "rosbag/bag.h"
#include "rosbag/view.h"
#include "std_msgs/String.h"
#include "std_msgs/Int32.h"

/* 
    需求：使用rosbag向磁盘文件读取数据（话题+消息）
    流程：
        1. 导包；
        2. 初始化；
        3. 创建rosbag对象；
        4. 读数据；
        6. 关闭文件流
 */

int main(int argc, char *argv[])
{

    setlocale(LC_ALL,"");

    ros::init(argc,argv,"bag_read");
    ros::NodeHandle nh;

    //创建 bag 对象
    rosbag::Bag bag;
    //打开 bag 文件
    bag.open("test.bag",rosbag::BagMode::Read);
    //读数据
    for (auto &&m : rosbag::View(bag))
    {
        std::string topic=m.getTopic();
        ros::Time time = m.getTime();
        std_msgs::StringPtr p = m.instantiate<std_msgs::String>();
        // if(p != nullptr){
        ROS_INFO("读取的话题:%s，时间戳：%.2f,消息值:%s",topic.c_str(), time.toSec(), p->data.c_str());
        // }
    }

    //关闭文件流
    bag.close();
    return 0;
}
