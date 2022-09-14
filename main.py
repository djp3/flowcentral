
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

def main():
    sam()


def charles():
    print("""
            You climb the ladder and find yourself holding a wrench to fix the pipe that renders air to the house.
            As you try to fix the pipe, you hear a loud noise coming from the basement. 

            Type 1 to go to the basement:

            Type 2 to go back to the ladder:

        """)

    choice = int(input("Type a number! "))

    if choice == 1:
        nancy()

    elif choice == 2:
        valentina()
        
    else:
        print("Bad answer!")

def trevor()
    print("""
            You enter the cave. You valiantly ignite your torch, but you notice it will soon fade.
            You gaze into the narrowing distant abyss. Behind a series of mossy stalagtites, there
            appears to be a hobbit and a goblin-like character having a picnic.
            
            Do you:
            1. Sneak up and kill them both, taking their food for yourself
            2. Join them for a wholesome meal
            
            Type a number!
            """)
    choice = int(input("Type a number! "))

    if choice == 1:
        todd()
    elif choice == 2:
        ethan()
    else:
        print("Bad answer!")
        
main()
