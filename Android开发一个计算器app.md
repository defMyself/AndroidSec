# Android开发一个计算器app

## 1.简介

运用Android Studio 实现一个计算器app

## 2. 实现原理

> 监听按钮，获取按钮对应的值，做出响应

* 数字按钮
  * 0 判断result是否为0， 不为0则拼接在result后面
  * 1-9 拼接在result后面
* 功能按钮
* 



源代码

```xml
//activity_main.xml

<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <GridLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:rowCount="6"
        android:columnCount="4"
        android:layout_marginHorizontal="15dp">

        <TextView
            android:id="@+id/showRst"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_columnSpan="4"
            android:layout_marginLeft="4px"
            android:gravity="left"
            android:text="0"
            android:textSize="50dip" />

        <Button
            android:id="@+id/clear"
            android:layout_width="352dp"
            android:layout_height="wrap_content"
            android:layout_columnSpan="4"
            android:text="清除"
            android:textSize="26sp" />
        <Button
            android:id="@+id/btn1"
            android:text="1"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn2"
            android:text="2"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn3"
            android:text="3"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnAdd"
            android:text="+"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn4"
            android:text="4"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn5"
            android:text="5"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn6"
            android:text="6"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnMinus"
            android:text="-"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn7"
            android:text="7"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn8"
            android:text="8"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn9"
            android:text="9"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnMulti"
            android:text="*"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnDot"
            android:text="."
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btn0"
            android:text="0"
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnEq"
            android:text="="
            android:textSize="26sp"/>
        <Button
            android:id="@+id/btnDvs"
            android:text="/"
            android:textSize="26sp"/>

    </GridLayout>

</android.support.constraint.ConstraintLayout>

```



```xml
//activity_main.xml

<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent" android:layout_height="match_parent" tools:context=".MainActivity">
    <GridLayout 
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:rowCount="6"
                android:columnCount="4"
                android:layout_marginHorizontal="15dp">
    	<TextView
                  android:id="@+id/showRst"
                  android:layout_width="wrap_content"
                  android:layout_height="wrap_content"
                  android:layout_columnSpan="4"
                  android:layout_marginLeft="4px"
                  android:gravity="left"
                  android:text="0"
                  android:textSize="50dip" />
        <Button
                android:id="@+id/clear"
                android:layout_width="352dp"
                android:layout_height="wrap_content"
                android:layout_columnSpan="4"
                android:text="清除"
                android:textSize="26sp" />
        <Button
                android:id="@+id/btn1"
                android:text="1"
                android:textSize="26sp" />
        <Button
                android:id="@+id/btn2"
                android:text="2"
                android:textSize="26sp" />
        <Button
                android:id="@+id/btn3"
    </GridLayout>
</android.support.constraint.ConstraintLayout>
```



```java
//MainActivity.java
package com.example.calculator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import andorid.widget.Button;
import android.widget.TextView;

import java.sql.Array;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {
    private TextView showRst;
    private Button btn1, btn2, btn3;
    private String progress, currentSymbol;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        showRst = (TextView) findViewById(R.id.showRst);
        btn1 = (Button) findViewById(R.id.btn1);
        btn2 = (Button) findViewById(R.id.btn2);
        btn3 = (Button) findViewById(R.id.btn3);
        
        btnAdd = (Button) findViewById(R.id.btnAdd);
        clear = (Button) findViewById(R.id.clear);
        
        btn1.setOnClickListener(new clickNum());
    }
    
}
```



























