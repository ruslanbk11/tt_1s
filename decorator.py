import time, random

def timer( function ):
    def wrapper( *args, **kwargs):
        print(args, kwargs)
        start_ts = time.time()
        result = function( *args, **kwargs)
        end_ts = time.time()
        print( "time of '{}' is '{}'".format(function.__name__, end_ts-start_ts))
        return result
    return wrapper

def sleeper( from_, to_ ):
    def sleeper_ (function):
        def wrapper( *args, **kwargs):
            time_to_sleep = random.randint( from_, to_)
            print('we gonna sleep {}'.format( time_to_sleep ))
            time.sleep(random.randint( from_, to_))
            result = function(*args, **kwargs)
            return result
        return wrapper
    return sleeper_

@sleeper(1,3)
@timer
def foo( a,b):
    time.sleep(5)
    return a+b

if __name__ == '__main__':
    print( foo(10, 5) )

