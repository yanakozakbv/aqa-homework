names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names:
    if not isinstance(name, str):
        continue
    print(name)
