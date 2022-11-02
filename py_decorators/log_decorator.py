import time

def log_generate(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt",'a') as l:
            l.write(f"Called Function {func.__name__} with arguments ({','.join([str(arg) for arg in args])}) at {time.strftime('%H:%M%p %Z on %b %d, %Y')} \n")
        func(*args, **kwargs)
    return wrapper

@log_generate
def add(a,b,c=9):
    return a+c+b

add(1,2)
