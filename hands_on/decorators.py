
import time


def log_func_name(func):
    def wrapper(*args):
        print(f'Function {func.__name__} started executing')
        return func(*args)  # returning the output from the actual function
    return wrapper


def log_func_time(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        print(f"Function took {time.time()-start_time}")
        return result
    return wrapper


'''Decorator functions gets called in the reverse order'''


@log_func_time
@log_func_name
def find_factorial(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    return product


if __name__ == '__main__':
    res = find_factorial(100000)
