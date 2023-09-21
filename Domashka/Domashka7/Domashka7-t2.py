import math


def square(side: float):
    P = 4 * side
    S = side * side
    D = math.sqrt(2) * side
    return P, S, D


if __name__ == '__main__':
    P, S, D = square(5)
    print(f"Perimetr = {P}, Square = {S}, Diagonal = {D}")
