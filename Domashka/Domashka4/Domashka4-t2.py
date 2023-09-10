CamelCase = ["FirstItem", "FriendsList", "MyTuple"]

snake_case = []
snake_word = ""

for word in CamelCase:
    snake_word += word[0]
    for letter in word[1:]:
        if letter.isupper():
            snake_word += '_'
        snake_word += letter

    snake_case.append(snake_word.lower())
    snake_word = ""
print(snake_case)
