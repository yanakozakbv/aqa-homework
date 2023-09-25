
def gen_range(range_num):
    num = 0
    for num in range(range_num + 1):
        if num % 2 == 0:
            yield num ** 2


if __name__ == '__main__':

    for i in gen_range(1000000000):
        print(i)
