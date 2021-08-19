var s = Java.use("java.lang.string"); 
var inner_class = Java.use("com.zhuotong.crackme$Innerclass")

Classname.$init.overload('[B').implementation = function(param) {
    // do something
}

Classname.$init.overload('[B', 'int', 'int').implementation = function(param1, param2, param3) {

}

Classname.func.oberload('int').implementation = function(param1) {

}

//invoke

var Classname = Java.use("com.crackme.apk.Classname")
var instance = Classname.$new()
instance.func()


var personclass = Java.use("com.crackme.Person")
var instance = personclass.$new()
instance.age.value = 10
instance.year.value = 100

console.log("test" + instance.age.value)


Java.perform(function() {

}
);