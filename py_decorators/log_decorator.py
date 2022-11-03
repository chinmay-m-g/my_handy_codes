import time

def log_generate(log_file):
  def logging(func):
    def wrapper(*args, **kwargs):
        with open(log_file,'a') as l:
            l.write(f"Called Function {func.__name__} with arguments ({','.join([str(arg) for arg in args])}) at {time.strftime('%H:%M%p %Z on %b %d, %Y')} \n")
        func(*args, **kwargs)
    return wrapper
  return logging

@log_generate(log_file="/home/chinmay/python_course/my_handy_codes/py_decorators/logs.txt")
def add(a,b,c=9):
    return a+c+b
   
add(1,2)
