import frida
import sys

jscode = """

"""
def on_message(message, data):
    if message['type'] == "send":
        print("[*] {}".format(message['payload']))
    else
        print(message)


session = frida.get_usb_device.attach("com.crackme.test")

script = session.create_script(jscode)

script.on("message", on_message)

script.load()

sys.stdin.read()

