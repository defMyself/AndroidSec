# Apk修改



## 流程

1. 反编译
2. 修改
3. 重新打包
4. 签名

## 工具

* `apktool`
* `dex2jar`
* `jd-gui`



1. 反编译

```shell
apktool d -o ouput_dir test.apk
```

2. 编译

```shell
apktool b -o ouput.apk input_dir
```

**apktool反编译出来的是smali文件，汇编版本，不是源码**

3. 源码获得

`dex2jar` 和`jd-gui`

```shell
d2j-dex2jar classes.dex
```

4. 使用`jd-gui`打开`classes-dex2jar.jar`

5. 使用`jarsigner`签名
6. 生成`keystore` `keytool`

```shell
keytool -genkey -alias demo.keystore -kayaly RSA -validity 40000 -keystore demo.key
```

7. 签名apk

```shell
jarsigner -verbose -keystore demo.keystore demo.akp demo.keystore
```



* proguard
* 