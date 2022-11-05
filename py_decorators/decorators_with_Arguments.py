import time
from datetime import datetime as dt
def prefix_decorator(prefix):
    def decorator_function(func):
        def wrapper_function(*args, **kwargs):
            time_string = r'%d %b %Y at %I:%M:%S:%f %p '
            print(prefix, "<- This is the decorator Argument")
            print("Function hierarchy prefix_decorator > decorator_function > wrapper_function")
            print(f"Function {func.__name__} started execution at {dt.now().strftime(time_string)}")
            val = func(*args, *kwargs)
            print(f"Function {func.__name__} completed execution at {dt.now().strftime(time_string)}")
            print(f"Function {func.__name__} returned {val}")
        return wrapper_function
    return decorator_function

@prefix_decorator("PREFIX : ")
def my_function(str1):
    return f"my_function argument is {str1}"

my_function("Chinmay")
my_function("Subhrajyoti")
my_function("Chanakya")
my_function("Subhadeep")
my_function("Gaurav")
