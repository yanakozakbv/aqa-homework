def display_box(width: int, height: int, character="*"):
    i = 0
    while i < height:
        j = 0
        while j < width:
            print(character, end='  ')
            j = j + 1
        i = i + 1
        print()


if __name__ == '__main__':
    display_box(5, 5)
