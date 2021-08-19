Interceptor.attach(Module.findExportByName("libc.so", "open"),
    onEnter: function(args) {
        send("open("+Memory.readString(args))
    }, 
    onLeave:function(retval){

    }
);