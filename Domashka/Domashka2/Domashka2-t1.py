#task 1
inp = input('Введіть температуру у Цельсіях:')

if inp.isnumeric() or (inp[0] == '-' and inp[1:].isnumeric()):

    cel = int(inp)
    far = float(cel * 9/5 + 32)
    kel = float(cel + 273.15)

    print("Температура у Фаренгейтах: ", far)
    print("Температура у Кельвінах: ", kel)

else:
    print("Введене значення не є числом")

