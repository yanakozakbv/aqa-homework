#task 2
import sys

inpV1 = input('Введіть кількість літрів V1:')
if not inpV1.isnumeric():
    print("Введене значення V1 не є числом")
    sys.exit()
V1 = float(inpV1)

inpV2 = input('Введіть кількість літрів V2:')
if not inpV2.isnumeric():
    print("Введене значення V2 не є числом")
    sys.exit()
V2 = float(inpV2)

inpT1 = input('Введіть температуру T1:')
if not inpT1.isnumeric():
    print("Введене значення T1 не є числом")
    sys.exit()
T1 = float(inpT1)

inpT2 = input('Введіть температуру T2:')
if not inpT2.isnumeric():
    print("Введене значення T2 не є числом")
    sys.exit()
T2 = float(inpT2)

temp = (V1 * T1 + V2 * T2) / (V1 + V2)
vol = (V1 + V2)

print("Температура суміші: ", temp)
print("Об'єм суміші: ", vol)
