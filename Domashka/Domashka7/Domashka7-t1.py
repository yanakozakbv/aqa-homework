def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start
    total = sum(range(start, end + 1))
    return total


if __name__ == '__main__':
    print(sum_range(5, 3))
