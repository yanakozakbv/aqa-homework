email = input("Введіть email:")

if email.count('@') == 1:
    sections = email.split('@')
    if '.' in sections[1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
