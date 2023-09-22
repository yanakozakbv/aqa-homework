def display_box(width: int, height: int, character="*"):
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if (i == 1 or i == height or
                    j == 1 or j == width):
                print(character, end="")
            else:
                print(" ", end="")

        print()


if __name__ == '__main__':
    display_box(10, 5)
    display_box(5, 4, "x")
