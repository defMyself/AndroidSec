# Android系统体系结构

开发APP主要是面向JavaAPI框架层进行开发。

* JavaAPI框架层
* 原生C/C++库 ： WebKit，OpenMAX，Libc, Media Framework, SGL, OpenGL ES, SQLite
* Android运行时：Android核心库和ART
* 硬件抽象层：Linux内核驱动的封装


## Android开发环境
1. Android Studio 
2. Android SDK
3. Android 模拟器


**SDK安装目录文件结构**
* build-tools: 存放不同版本的Android项目编译工具
* docs: 存放Android SDK开发文件和API文档等
* emulator：
* extra：USB驱动，Intel的硬件加速包等
* platforms : 
* platforms-tools:
* sources : Android 源码
* system-image： 系统镜像
* tools：Android开发，调试工具

**Monitor工具使用**

## Android开发应用
1. 创建项目
2. 在XML布局文件中定义用户界面
3. Java编写业务代码



*Android 9.0对应API 28*

```json
dependencies {

    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
}

```

build.gradle文件中配置国内中央仓库


android开发者重点关注的两个目录：`app/src/main/java` 和 `app/scr/main/res`

## Android基本组件
```java
setContentView()
LinearLayout layout = new LinearLayout(this);
setContentView(layout);
```

**`BroadcastReceiver`**的两种注册方法
1. 代码中`Context.registerReceiver()`
2. AndroidManifest.xml文件中注册<receiver../>

**ContentProvider**: 跨应用数据交换
实现一个ContentProvider需要实现的抽象方法：
*  `insert(Uri, ContentValues)
* `delete(Uri, ContentValues)`
* `update(Uri, ContentValues, String, String[])`
* `query(Uri, String[], String, String[], String)`

ContentProvider暴露数据
ContentResolver访问数据

### Intent和IntentFilter
通信载体

> 当需要启动一个Activity时，可调用`Context`的`startActivity(Intent intent)`方法
`startActivityForResult(Intent intent, int requestCode`
**Intent参数封装了需要启动的目标的Activity信息**

* 当需要启动一个Service时，可调用`Context`的startService(Intent intent)方法或bindService(Intent service, ServiceConnection conn, int flags)方法，其中Intent参数封装了要启动目标的信息

* 触发BroadcastReceiver时，可调用Context的sendBroadcast(Intent intent),sendStickyBroadcast(Intent intent)和sendOrderedBroadcast(Intent intent, String receiverPermission)

* 显示Intent
* 隐示Intent


