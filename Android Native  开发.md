# Android Native  开发

## 00 NDK 开发

NDK英文全称为native development kit, 简称NDK， 是一种基于原生程序接口的软件开发工具。通过此工具开发的程序直接以本地语言运行，而非虚拟机。所以只有像Java这种运行在虚拟机中的语言才会有原生开发工具包。

* NDK 包括一系列工具

  > NDK提供了一系列工具，帮助开发者快速开发C/C++的动态库，并能够将so和java应用一起打包成apk

* NDK集成了交叉编译器，并提供了相应的mk文件隔离CPU、平台、ABI等差异，开发人员只需要简单修改mk文件，就可以创建出so

  > NDK可以自动地将so和Java应用一起打包，极大地减轻了开发人员的打包工作

  

## 01 使用NDK开发的原因

1. 保护代码。Java层的代码是很容易被反编译的，C/C++库的反汇编难度较大。
2. 代码重用。现存的开源库是使用C/C++代码编写的。
3. 提高应用程序的执行效率。将要求高性能的应用逻辑使用C开发，从而提高程序的执行效率。
4. 便于移植。用C/C++写的库可以方便地在其他嵌入式平台上再次使用。

## 02 开发前准备

* Android Studio 2.2
* JDK 1.7
* API 24
* Gradle 2.2.2

### NDK和CMake的下载和安装





# NDK使用入门

> 目录
>
> 下载NDK和工具
>
> 创建或导入原生项目

原生开发套件（NDK)是一套工具，是您能够在Android应用中使用C和C++代码，并提供众多平台库

可以使用这些平台库管理原生Activity和访问实体设备组件，比如传感器和触摸输入。

* 降低延迟或运行游戏或物理模拟等计算密集型应用。
* 重复使用您自己或其他开发者的C或C++库



**Android Studio2.2及以上版本使用NDK将C和C++代码编译到原生库中，然后通过Android Studio的集成构建系统Gradle将原生库打包到APK中。**

Java代码随后可以通过Java原生接口（JNI)框架调用原生库中的函数。



Android Studio编译原生库的默认构建工具CMake。由于很多现有的项目都使用ndk-build构建工具包，因此Android Studio也支持ndk-build。

如果创建新的原生库，则应使用CMake。



**编译和调试原生代码所需要的组件：**

* NDK
* CMake
* LLDB

### 1. 创建或导入原生项目



### 1. 创建支持C/C++的新项目

1. 在向导的Choose your project部分中，选择Native C++项目类型
2. Next
3. 填写向导下一部分中的所有其他字段
4. Next
5. 向导的Customize C++ Support部分中，您可以使用C++ Standard字段自定义项目。在Toolchain Default可以使用默认的CMake
6. 点击Finsh































