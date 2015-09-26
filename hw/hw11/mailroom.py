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
        not_done = False
        return not_done
    else:
        print("INVALID INPUT.")
        print("")
        return home_menu()


def create_report(donor_list):
    """Prints a list of donors, sorted by total donation amount"""
    pass


def send_thank_you():
    """Prompt user for full name of donor"""

    print("")
    print("Please enter a name, or choose from the following: ")
    print("")
    print("list - Print a list of previous donors")
    print("")
    print("quit - Return to main menu")
    print("")

    donor_name = input("> ")
    str_donor = str(donor_name)

    if str_donor == "list":
        print("")
        for donor in donor_list:
            print(donor[0])
        return send_thank_you()
    elif str_donor == "quit":
        return home_menu()
    else:
        for donor in donor_list:
            if donor[0] == str_donor:
                donation = get_donation()
                donor[1] += donation
                donor[2] += 1
                break
            else:
                donation = get_donation()
                donor_list.append([str_donor, donation, 1])
                break

    create_letter(str_donor, donation)


def get_donation():
    """ Prompt user for amount of donation """

    print("")
    print("Please enter a donation amount or 'quit':")
    print("")

    donation = (input("> "))

    donation = is_float(donation)
    donation = str('%.2f' % donation)
    return(donation)


def is_float(donation):
    """ Evaluates donation to see if it is convertable to a float

    return value if it is
    run get_donation if it is not

    """

    try:
        val = float(donation)
        return val
    except ValueError:
        print("INVALID INPUT!")
        return get_donation()


def create_letter(str_donor, donation):
    print("")
    print("Dear %s," % str_donor)
    print("")
    print("Thank you for your donation of $%s. We here at the Foundation for "
          "Homeless Whales greatly appreciate it. Your money will go towards "
          "creating new oceans for whales to live in." % donation)
    print("")
    print("Thanks again,")
    print("")
    print("Kyle Winckler")
    print("")
    print("Director, F.H.W")
    print("")
    print("Press Enter to Continue...")
    print("")


if __name__ == '__main__':

    not_done = True

    donor_list = [
        ["Neal Stephenson", 2000, 3],
        ["Luigi Mario", 1200, 1],
        ["Ellie Arroway", 1700, 2],
        ["Kevin Flynn", 1100, 2],
        ["Severus Snape", 5, 1]
    ]

    while not_done:
        not_done = home_menu()
