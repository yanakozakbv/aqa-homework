#task1
import sys

word = input("Введіть слово:")

if not word.isalpha():
    print("Це не є словом")
    sys.exit()

if word[0::] == word[::-1]:
    print("+")
else:
    print("-")
