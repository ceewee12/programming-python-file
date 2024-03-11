def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300
def myfunc():
    print("inside function",x)
    
myfunc()

print("",x)

def my_func():
    global x
    x = 300