import frida
import sys
rdev = frida.get_remote_device()
session = rdev.attach("com.tencent.mm")

scr = """
Java.perform(function () {
var ay = Java.use("com.tencent.mm.sdk.platformtools.ay");
ay.pu.implementation = function(){
    var type = arguments[0];
    send("type="+type);
    if (type == 2)
    {
    return this.pu(type);
    }
    else
    {
    return 5;
    }
};

});
"""

script = session.create_script(scr)
def on_message(message ,data):
    print message
script.on("message" , on_message)
script.load()
sys.stdin.read()
