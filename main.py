def main():
    sam()


def sam():
    print("""
            You're walking in a deep, dark forest. You find a ladder hanging from a tree,
            leading up into the mist. Alternatively, a dark cave looms out of a nearby rock
            outcropping.

            Do you:
            1. Take the ladder
            2. Enter the cave

            Type a number!
            """)
    choice = int(input("Type a number! "))

    if choice == 1:
        charles()
    elif choice == 2:
        trevor()
    else:
        print("Bad answer!")


main()
