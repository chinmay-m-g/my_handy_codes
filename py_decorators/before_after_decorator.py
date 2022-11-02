#Python Decorators Example 1
import time 

def before_after(f):
    def wrapper(*args):
        print("Before")
        f(*args)
        print("After")
    return wrapper
    
@before_after    
def decorated_function(input_argument):
    print("Function Run:", input_argument)
	
decorated_function("Call from Main")

print("*"*50, "Call From a Class", "*"*50)
class Test:
    @before_after
    def decorated_method(self) -> None:
        print("Run Method inside Test Class")

t=Test()
t.decorated_method()
