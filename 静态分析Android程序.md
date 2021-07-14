# 静态分析Android程序

> 阅读反汇编代码
>
> 1. 阅读Dalvik字节码
> 2. 阅读baksmali反编译生成的smali文件
> 3. 阅读Java源码
> 4. dex2jar，使用jd-gui阅读jar文件的代码

## smali代码

每个DEX文件中的内部类在反编译时会使用单独的smali文件存放