#task 3

firstnum = float(input("Введіть перше число: "))
secondnum = float(input("Введіть друге число: "))
print("""Доступні арифметичні операції:
                                1. +
                                2. -
                                3. * 
                                4. /""")
operation = input("Введіть індекс бажаної операції: ")

if operation == 1:
    print("Result=",float(firstnum+secondnum))
elif operation == 2:
    print("Result=", float(firstnum - secondnum))
elif operation == 3:
    print("Result=", float(firstnum * secondnum))
elif operation == 4:
    print("Result=", float(firstnum / secondnum))
else:
    print("Введене значення не є коректним")
