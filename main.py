
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

def trevor():
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

def ethan():
    print("""
            You meekly walk up to the hobbit and his curious looking friend. 
            They invite you over and you gladly accept. 
            Luckily, they have some potatoes, boiled, mashed, and stuck in a stew with a nice definitely dead rabbit. 
            As you were sharing this lovely meal with a couple lads a newsrunner runs by and delivers the news of
            the destruction of the one ring. You all celebrate together and feast late into the night. Each one 
            dreaming and reflecting on the wonderful company of two complete strangers. None of them ever forgot that
            night and they told the story to their children for years to come. :)
            """)
        
main()
def nancy():
    print("""
            You are brave and decide to face the noise in the basement. You go
            down the steps and find...several people playing dice. You join them!
            """)

def todd():
    print("""
            You prepare to ambush the creatures and manage to get your arms around the neck of the goblin.
            You failed to realize that these cave creatures are armed and soon meet a bloody death at the
            hand of the hobbit and his knife.

            THE END.
        """)

def valentina():
    print(
        """
        Wow! Now you have a great view of your house! 

        After a sigh of relief, you realize that you are very hugry. A perfect time for a nice picnic.
        """)

def ethan():
    print("""
            You meekly walk up to the hobbit and his curious looking friend. 
            They invite you over and you gladly accept. 
            Luckily, they have some potatoes, boiled, mashed, and stuck in a stew with a nice definitely dead rabbit. 
            As you were sharing this lovely meal with a couple lads a newsrunner runs by and delivers the news of
            the destruction of the one ring. You all celebrate together and feast late into the night. Each one 
            dreaming and reflecting on the wonderful company of two complete strangers. None of them ever forgot that
            night and they told the story to their children for years to come. :)
            """)
        
sam()
