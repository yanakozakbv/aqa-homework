from Domashka8_t2 import gen_range
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Execution time: {duration}")
        return result
    return wrapper


@execution_time
def gen(num):
    for i in gen_range(num):
        print(i)
    return


@execution_time
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(divide(210, 13))
    print("="*100)
    gen(16)

