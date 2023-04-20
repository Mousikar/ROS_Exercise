#include "ros/ros.h"
/* 演示参数查询
    实现：
        param(键,默认值) 
            存在，返回对应结果，否则返回默认值

        getParam(键,存储结果的变量)
            存在,返回 true,且将值赋值给参数2
            若果键不存在，那么返回值为 false，且不为参数2赋值

        getParamCached键,存储结果的变量)--提高变量获取效率
            存在,返回 true,且将值赋值给参数2
            若果键不存在，那么返回值为 false，且不为参数2赋值

        getParamNames(std::vector<std::string>)
            获取所有的键,并存储在参数 vector 中 

        hasParam(键)
            是否包含某个键，存在返回 true，否则返回 false

        searchParam(参数1，参数2)
            搜索键，参数1是被搜索的键，参数2存储搜索结果的变量

    ros::param ----- 与 NodeHandle 类似
    修改：
        继续调用setparam或set函数，保证键是已经存在的，值会覆盖
*/
int main(int argc, char *argv[])
{
    // 设置编码
    setlocale(LC_ALL,"");
    // 初始化ros节点
    ros::init(argc,argv,"get_paam_c");
    // 创建节点句柄
    ros::NodeHandle nh;
    // 1.param
    double radius=nh.param("radius",0.5);
    ROS_INFO("radius=%.2f",radius);
    // 2.getParam
    double radius2=0.0;
    // bool result=nh.getParam("radius",radius2);
    // 3.getParamCached与getParam类似，只是性能上有提升，一般测试下，看不出来
    bool result=nh.getParamCached("radiusyyy",radius2);
    if(result){
        ROS_INFO("获取的半径是：%.2f",radius2);
    }else{
        ROS_INFO("被查询的变量不存在！");
    }
    // 4.getaParamNames
    std::vector<std::string> names;
    nh.getParamNames(names);
    for(auto &&names:names){
        ROS_INFO("遍历到的元素：%s",names.c_str());
    }
    // 5.hasParam
    bool flag1=nh.hasParam("radius");
    bool flag2=nh.hasParam("raadius");
    ROS_INFO("radius存在吗？%d",flag1);
    ROS_INFO("radius存在吗？%d",flag2);
    // 6.searchParam
    std::string key;
    nh.searchParam("radius",key);
    ROS_INFO("搜索结果：%s",key.c_str());
    std::string key1;
    nh.searchParam("radiius",key1);
    ROS_INFO("搜索结果：%s",key1.c_str());

    // ros::param
    double radius_param=ros::param::param("radius_paaram",100.5);
    ROS_INFO("radius_param=%.2f",radius_param);

    std::vector<std::string> names_param;
    ros::param::getParamNames(names_param);
    for(auto &&name:names_param){
        ROS_INFO("遍历到的元素：%s",name.c_str());
    }
    
    return 0;
}
