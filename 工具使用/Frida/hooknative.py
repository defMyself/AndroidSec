import frida
import sys
rdev = frida.get_remote_device()
session = rdev.attach("com.tencent.mm")
scr = """
Interceptor.attach(Module.findExportByName("libc.so" , "open"), {
    onEnter: function(args) {
        send("open("+Memory.readCString(args[0])+","+args[1]+")");
    },
    onLeave:function(retval){
    
    }
});
"""
script = session.create_script(scr)
def on_message(message ,data):
    print message
script.on("message" , on_message)
script.load()
sys.stdin.read()
