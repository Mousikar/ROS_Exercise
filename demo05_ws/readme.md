# demo05_ws

1. urdf01_rviz

`roslaunch urdf01_rviz demo01_helloworld.launch`

`roslaunch urdf01_rviz demo02_link.launch`

`roslaunch urdf01_rviz demo03_joint.launch`

带有注释版本的demo05_ws/src/urdf01_rviz/urdf/urdf/demo03_joint.urdf
```
<!-- 需求：设置机器人底盘，并添加摄像头 -->
<robot name="mycar">
    <!-- 1. 底盘link -->
    <link name="base_link">
        <!-- 可视化标签 -->
        <visual>
            <!-- 形状 -->
            <geometry>
                <!-- 立方体 -->
                <box size="0.3 0.2 0.1" />                
            </geometry>
            <origin xyz="0 0 0" rpy="0 0 0" />
            <material name="car_color">
                <color rgba="0.8 0.5 0 0.5" />
            </material>
        </visual>
    </link>

    <!-- 2. 摄像头link -->
    <link name="camera">
        <!-- 可视化标签 -->
        <visual>
            <!-- 形状 -->
            <geometry>
                <!-- 立方体 -->
                <box size="0.02 0.05 0.05" />                
            </geometry>
            <!-- 先使用默认（后期修改） -->
            <origin xyz="0 0 0.025" rpy="0 0 0" />
            <!-- <origin xyz="0 0 0.025" rpy="0 0 0" /> -->
            <material name="camera_color">
                <color rgba="0 0 1 0.5" />
            </material>
        </visual>
    </link>

    <!-- 3. 关节 -->
    <joint name="camera2base" type="continuous">
        <!-- 父级link -->
        <parent link ="base_link"/>
        <!-- 子级link -->
        <child link ="camera" />
        <!-- 设置偏移量 -->
        <origin xyz="0.12 0 0.05" rpy="0 0 0" />
        <!-- 设置关节旋转参考坐标轴 -->
        <axis xyz="0 0 1" />
    </joint>
</robot>
```

如果没有ros-melodic-joint-state-publisher-gui，则安装一下：

`sudo apt-get install ros-melodic-joint-state-publisher-gui`

抖动是因为joint_state_publisher与joint_state_publisher_gui发布消息叠加导致的，可以把前面的joint_state_publisher注释掉

`roslaunch urdf01_rviz demo04_base_footprint.launch`

fixed frame 改成 base_footprint
![图片](https://user-images.githubusercontent.com/103837402/233761152-62256d22-51ce-42a0-bd42-ce09161278ce.png)
