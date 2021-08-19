import frida

rdev = frida.get_remote_device()
session = rdev.attach("com.crackme.test")

modules = session.enumerate_modules()

for module in modules:
    print(moudle)
    export_functions = modules.enumerate_exports()

    for func in exports_functions:
        print("{} : {}".format(func.name, hex(func.relative_address)))
