# run urdf02_gazebo
`roslaunch urdf02_gazebo demo01_helloworld.launch`

# 需要提前安装 Arbotix

## 方式1:命令行调用

`sudo apt-get install ros-<<VersionName()>>-arbotix`

将 <<VsersionName()>> 替换成当前 ROS 版本名称，如果提示功能包无法定位，请采用方式2。

## 方式2:源码安装

先从 github 下载源码，然后调用 catkin_make 编译

`git clone https://github.com/vanadiumlabs/arbotix_ros.git`

# 命令行控制Gazebo中的小车移动
`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

如果要修改速度：
`rosrun teleop_twist_keyboard teleop_twist_keyboard.py _speed:=0.3 _turn:=0.5`
![图片](https://user-images.githubusercontent.com/103837402/235341809-2b85f630-abfc-413b-9de1-9171a808c0a0.png)

### 先启动仿真环境：

`roslaunch urdf02_gazebo demo03_env.launch`

### 然后打开rviz：

`roslaunch urdf02_gazebo demo04_sensor.launch`

### 最后启动键盘控制节点：

`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

![图片](https://user-images.githubusercontent.com/103837402/235342213-551b6967-9f50-4c78-8e38-7b95fd3dfecc.png)

![图片](https://user-images.githubusercontent.com/103837402/235342567-bb460ba4-9afa-4fac-9d5a-52377535ee97.png)

![图片](https://user-images.githubusercontent.com/103837402/235342552-0381ba51-3566-4bd8-ab90-a99efcfd48c6.png)

### 加入摄像头
`rostopic pub -r 10 /cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.50"`

![图片](https://user-images.githubusercontent.com/103837402/235343010-af66e5c8-bd45-4a0e-bc24-d37f589d414a.png)

![图片](https://user-images.githubusercontent.com/103837402/235344034-63429a50-585b-475b-bd2c-68ac2b744464.png)
