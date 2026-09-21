# DECORATOR MINI PROJECT
import functools
import time

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        differnce = end - start
        print("difference is :",differnce)
    return wrapper

def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("values are :",*args,**kwargs)
        result = func(*args,**kwargs)
        return result
    return wrapper

def validation_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        for value in args:
            if value < 0:
                print("INVALID VALUE")
            else:
                fresult = func(*args,**kwargs)
                return fresult
    return wrapper

@timing_decorator
@logging_decorator
@validation_decorator
def calculate_price(price, percent):
    finalprice = price - (price * percent / 100)
    print("final price is :", finalprice)

calculate_price(1000,10)










