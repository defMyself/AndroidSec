# Android应用的界面编程

### 1. 界面编程与视图组件View
View组件代表了一个空白的矩形区域
View的子类：ViewGroup通常作为其他组件的容器使用
组合器设计模式：

*实现一个跟随手指的小球*：
开发自定义的UI组件，在指定位置绘制一个小球，程序监听手指的动作，并传递给组件，通知组件重绘

```java
public class DrawView extends View
{
    private float currentX = 40f;
    private float currentY = 50f;

    private Paint p = new Paint();

    public DrawView(Context context)
    {
        super(context);
    }
    public DrawView(Context context, AttributeSet set)
    {
        super(context, set);
    }
    @Override
    public void onDraw(Canvas canvas)
    {
        super.onDraw(canvas);
        p.setColor(Color.RED);
        canvas.drawCircle(currentX, currentY, 15F, p);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event)
    {
        currentX = event.getX();
        currentY = event.getY();

        invalidate();
        return true;
    }
}
```


```java
public class MainActivity extends Activity
{
    @Override
    public void onCreate(Bundle saveInstanceState)
    {
        super.onCreate(savedInstanceState)；
        setContentView(R.layout.activity_main);
        LinearLayout root = findViewById(R.id.root);
        DrawView draw = new DrawView(this);

        draw.setMinimumWidth(300);
        draw.setMinmumHeight(500);
        root.addView(draw);
    }
}

```

## 2.布局管理器


```java
TextView hello = new TextView(this);
hello.setText("Hello Android");

// ConstraintLayout
```

* 线性布局： `LinearLayout`
* 表格布局： `TableLayout`
* 帧布局：`FrameLayout`
* 绝对布局： `AbsoluteLayout`
* 约束布局：``

> 为何不直接在run()方法里直接更新TextView的背景色呢？
回答： Android的View和UI组件不是线程安全的，所以Android不允许开发者启动线程访问用户界面的UI组件。


##  3. TextView及其子类
所有的UI界面都是先创建容器，即ViewGroup的实例

```java

```

## 4. ImageView及其子类

子类
* ImageButton
* ZoomButton

## 5. AdapterView及其子类
1. AdapterView继承自ViewGroup，本质是一个容器
2. 子类AbsListView,AbsSpinner,AdapterViewAnimator

### Adapter接口及实现类
Adapter本身是一个接口，派生了ListAdapter和SpinnerAdapter两个子接口
* `ListAdapter`为`AbsListView`提供列表项
* `SpinnerAdapter`为`AbsSpinner`

```java
ArrayAdapter adapter1 = new ArrayAdapter(this, R.layout.array_item, arr1);
list1.setAdapter(adapter1);
ListView list2 = findViewById(R.id.list2);

```

* AutoCompleteTextView
* ExpandableListView
* Spinner
* AdapterViewFlipper
* StackView
* RecyclerView
* ProcessBar
* SeekBar
* RatingBar
* ViewAnimator
* ViewSwitcher
* ImageSwitcher
* TextSwitcher
* ViewFlipper
* SearchView
* ScrollView


一些杂项组件：
* Toast显示提示信息
Toast提示信息不会获得焦点
Toast提示信息过一段时间会自动消失

### Spinner的功能和用法
Spinner是一个列表选择框


## 对话框
1. AlertDialog
2. ProgressDialog
3. DatePickerDialog
4. TimePickerDialog

## 菜单


