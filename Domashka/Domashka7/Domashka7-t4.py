def to_double(x):
    return 2 * x


def to_triple(x):
    return 3 * x


def my_map(callback, iterable):
    result = []
    for item in iterable:
        result.append(callback(item))
    return result


numbers = [3, 4, 0, 10, 1]
doubles = my_map(to_double, numbers)
triples = my_map(to_triple, numbers)
quarters = my_map(lambda x: 4 * x, numbers)

if __name__ == '__main__':
    print(doubles)
    print(triples)
    print(quarters)