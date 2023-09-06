#task5

ip = input("Введіть IP адресу:")

sections=ip.split('.')
if len(sections) != 4:
    print("Неправильна IP-адреса 5")
else:
    if 0 <= int(sections[0]) <= 255 and 0 <= int(sections[1]) <= 255 and 0 <= int(sections[2]) <= 255 and 0 <= int(sections[3]) <= 255:
        print("правильна IP-адреса")
    else:
        print("Неправильна IP-адреса 11")