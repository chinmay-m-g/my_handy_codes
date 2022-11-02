import time

def timer(f):
    def wraper(*args, **kwargs):
        start_time= time.time()
        f(*args, **kwargs)
        print(f"Function {f.__name__} with argument {args[0]} took : ", abs(start_time - time.time()),"Seconds to Execute")
    return wraper

@timer
def decorated_function(n:int)->None:
    time.sleep(n)

for i in range(1,11):
    decorated_function(i)
