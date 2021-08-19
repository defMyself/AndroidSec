if(Java.avaliable) {
    Java.perform(function() {
        var MainClass = Java.use("com.crackme.MainActivity");
        MainClass.isExcellent.implementation = func(para1, para2) {
            return true;
        }
    }
    )
}

