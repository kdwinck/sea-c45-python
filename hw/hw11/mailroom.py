donor_list = [
    ["Neal Stephenson", 2000, 3],
    ["Luigi Mario", 1200, 1],
    ["Ellie Arroway", 1700, 2],
    ["Kevin Flynn", 1100, 2],
    ["Severus Snape", 5, 1]
]


def introduction():
    """ Print out the introduction for the user"""

    print("")
    print("Welcome to Mailroom Madness")
    print("")
    print("Choose from the following:")
    print("")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program")
    print("")


def home_menu():
    """user chooses between sending thank you, creating report,
       or exiting the program
    """
    introduction()

    user_choice = input("> ")
    user_choice = user_choice.upper()  # convert input to upper case

    if user_choice == "T":
        pass
    elif user_choice == "R":
        pass
    elif user_choice == "QUIT":
        pass
    else:
        print("Invalid input.")
        home_menu()


home_menu()
