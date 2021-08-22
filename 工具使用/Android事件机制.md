# Android事件机制
* Android提供的两种事件处理机制：基于监听的事件处理，基于回调的事件处理

绑定事件监听器：
```java
dateBn.setOnClickListener(view-> {
    Calendar c = Calendar.getInstance();
    new DatePickerDialog(MainActivity.this, 
        // 绑定监听器
        （dp, year, month, dayOfMonth) -> {
            show.setText("has chosen", + year)
        }, c.get(Calendar.YEAR),
           c.get(Calendar.MONTH),
           c.get(Calendar.DAY_OF_MONTH))
        .show();
});
```

### 2.基于监听的事件处理
1. 事件源
2. 事件
3. 事件监听器

```java
Event Source
Event
Event Listener
```
基于监听的事件处理机制是一种委派式（Delegation)事件处理方式：
* 普通组件将整个事件处理委托给特定的对象，当该事件源发生指定的事件时，就通知所委托的事件监听器，由事件监听器来处理这个事件
监听器类必须由开发者来实现

```java
public class MainActivity extends Activity
{
    @Override
    protected void onCreate(Bundle saveInstanceState)
    {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_main);
        Button bn = findViewById(R.id.bn);
        bn.setOnClickListener(new MyClickListener());
    }

    class MyClickListener implements View.OnClickListener
    {
        @Override
        public void onClicker(View v)
        {
            TextView txt = findViewById(R.id.txt);
            txt.setText("Clicked");
        }
    }
}
```

**基于监听的事件处理模型的编程步骤**
1. 获取普通界面组件，事件源，被监听的对象
2. 实现事件监听器类，该监听器是一个特殊的类，必须实现一个XxxListener接口
3. 调用事件源的setXxxListener方法将事件监听器对象注册给普通组件，事件源

* 内部类作为事件监听器类
* Activity本身作为事件监听器类
* Lambda表达式作为事件监听器类
* 

### 基于回调的事件处理
* 集成GUI组件类，重写事件处理方法

### 基于回调的事件传播
### 响应系统设置的事件


**获取系统设备状态**

### Handler消息传递机制

**只允许UI主线程修改Activity里的UI组件**
`Handler`类的主要作用：
1. 在新启动的线程中发送消息
2. 在主线程中获取，处理消息

> 当新启动的线程发送消息时，消息会发送到与之关联的`MessageQueue`, 而`Handler`会不断地从MessageQueue中获取并处理消息---这将导致Handler类中处理消息的方法被回调

```java
handleMessage(Message msg)
hasMessages(int what)
hasMessages(int what, Object object)
Message obtainMessage()
sendEmptyMessage（int what)
sendEmptyMessageDelayed(int what, long delayMillis)
sendMessage()
```

### Handler,Loop,MessageQueue的工作原理

* `Message`: Handler接受和处理的消息对象
* `Looper`: 每个线程只能拥有一个Looper,其中loop方法负责读取MessageQueue中的消息
* `Message`: 消息队列


```java
public static final void prepared()
{
    if(sThreadLocal.get() != null)
    {
        throw new RuntimeException("Only one Looper per thread");
    }
    sThreadLocal.set(new Looper());
}
```

ANR线程


```java
class CalThread extends Thread
{
    private Handler mHandler;
    @Override
    public void run()
    {
        Looper.prepare();
        mHandler = new Handler()
        {
            @Override public void handleMessage(Message msg)
            {
                if(msg.what == 0x123) {

                }
            }
        };
        Looper.loop();
    }
}
```

## 异步任务 `AsyncTask`

例子：使用异步任务执行下载

