
def my_decorator(func):
    def wrapper(*args, **kwargs):
        function_result = func(*args, **kwargs)
        result = f'{function_result} it was {func.__name__} function'
        return result
    return wrapper


@my_decorator
def addition(a, b):
    return a + b


@my_decorator
def multiplexion(a, b):
    return a * b


if __name__ == '__main__':
    print(addition(210, 13))
    print(multiplexion(210, 13))