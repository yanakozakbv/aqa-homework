programing = {"Java": "James Gosling", "Python": "Guido van Rossum", "C": "Dennis Ritchie", "PHP": "Rasmus Lerdorf" }
language_to_delete = ""
print_collection = True

while True:
    if print_collection:
        print_collection = False
        for k, v in programing.items():
            print("".join(["My favorite programming language is ", k, ". It was created by ", v]))

    if len(programing.items()) == 3:
        break

    language_to_delete = input("Input language to delete: ")
    if language_to_delete in programing.keys():
        programing.pop(language_to_delete)
        print_collection = True
    else:
        print("There is no such language in dictionary")