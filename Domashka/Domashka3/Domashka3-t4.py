text = input("Введіть текст:")

my_list = text.split()
print(my_list)

if len(my_list) < 3:
    print("Кількість елементів менша за 3. Кількість елементів:", len(my_list))
else:
    print(my_list[-3:])

