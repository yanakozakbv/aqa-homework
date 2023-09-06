text = input("Введіть текст:")
word = input("Введіть слово:")


my_list = text.split()
if word in my_list:
    print("Yes")
else:
    print("No")