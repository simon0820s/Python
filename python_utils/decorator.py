from datetime import datetime


def execution_time(func):
    def wrapper():
        initial_time=datetime.now()
        func()
        final_time=datetime.now()
        time_elapsd=final_time-initial_time
        print("delay: "+str(time_elapsd.total_seconds())+"s")
    return wrapper

@execution_time
def func():
    for _ in range(1,1000):
        pass
func()

def sum(a:int,b:int)->int:
    return a+b