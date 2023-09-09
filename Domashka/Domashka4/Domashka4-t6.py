letters = {}
for c in input("Please input your text: "):
    if letters.get(c, 0) == 0:
        letters[c] = 1
    else:
        letters[c] += 1

final = " ".join(key + ',' + str(value) for key, value in letters.items())
print(final)
