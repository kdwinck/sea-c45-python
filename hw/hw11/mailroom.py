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
        send_thank_you()
    elif user_choice == "R":
        create_report(donor_list)
    elif user_choice == "QUIT":
        pass
    else:
        print("INVALID INPUT.")
        home_menu()


def create_report(donor_list):
    """Prints a list of donors, sorted by total donation amount"""
    pass


def send_thank_you():
    """Prompt user for full name of donor"""

    print("Please enter a name, or choose from the following: ")
    print("")
    print("list - Print a list of previous donors")
    print("")
    print("quit - Return to main menu")
    print("")

    donor_name = input("> ")
    str_donor = str(donor_name)

    if str_donor == "list":
        print(donor_list)
        print("")
        send_thank_you()
    elif str_donor == "quit":
        home_menu()
    else:
        for donor in donor_list:
            if donor[0] == str_donor:
                donation = get_donation()
                donor[1] += donation
                donor[2] += 1
                break

        donation = get_donation()
        donor_list.append([str_donor, donation, 1])
    print(donor_list)


def get_donation():
    print("")
    print("Please enter a donation amount or 'quit':")
    print("")

    donation_amount = int(input("> "))
    return(donation_amount)

home_menu()
