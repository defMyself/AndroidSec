# APK壳的特征



**1. 爱加密加固:**

爱加密加固一般有两个 Application 入口类，为 SuperApplication 和 NativeApplication，壳的入口点为com.shell.SuperApplication，assets 目录下有  ijiami.dat、ijiami2.dat、ijiami.ajm，壳的 so 为 libexec.so 和  libexecmain.so，它们可能在 libs 目录或 assets 目录中。

**2. 梆梆加固:**

Assets 目录下有 secData0.jar，libs 目录下为  libSecShell.so、libSecShell_x86.so、libSecShell_art.so  等，壳为com.secshell.shellwrapper.SecAppWrapper。

**3. 360 加固:**

Assets 目录下常有：libjiagu.so\libjiagu_ls.so\libjiagu_x86.so\libjiagu_art.so 等，壳的  application 常为 com.stub.StubApp，以前版本可能为 com.stub.stubxxxx，壳的入口为  com.stub.stub01.Stub01。

**4. 阿里云加固:**

Assets 目录下为 libdemolishdata.so，libs 目录下为 libdemolish.so，壳的入口点一般为原入口点，但方法都是抽取并 native 的。

**5. 腾讯乐固:**

Libs 目录常为：liblegudb.so、libshella-2.10.2.3.so、mix.dex，壳的入口点为 com.tencent.StubShell.TxAppEntry。

**6. 百度加固:**

Assets 目录和 libs  目录经常有：libbaiduprotect.so、libbaiduprotect_x86.so、libbaiduprotect_art.so、baiduprotect1.jar 等，壳的入口点为 com.baidu.protect.StubApplication。

**7. 娜加加固:**

Libs 目录一般拥有 libddog.so、libcdog.so、libfdog.so 等。

**8. 顶象加固:**

此加固并不常见，一般 libs 目录有个 libjni.so 或 libsec.so，入口点为原入口点，也是全 native 的，但全是在 so 里就利用 arm 编写了对应方法。