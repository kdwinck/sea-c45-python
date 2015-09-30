import operator


def introduction():
    """ Print out the introduction for the user"""

    print()
    print("Welcome to Mailroom Madness")
    print()
    print("Choose from the following:")
    print()
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program")
    print()


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
        print()
        return home_menu()


def send_thank_you():
    """Prompt user for full name of donor"""

    print()
    print("Please enter a name, or choose from the following: ")
    print()
    print("list - Print a list of previous donors")
    print()
    print("quit - Return to main menu")
    print()

    donor_name = input("> ")
    str_donor = str(donor_name)
    names = name_list()

    if str_donor == "list":
        print("")
        for key in donor_list:
            print(key)
        return send_thank_you()
    elif str_donor == "quit":
        return home_menu()
    elif str_donor in names:
        for key in donor_list:
            if key == str_donor:
                donation = get_donation()
                donor_list[key][0] += donation
                donor_list[key][1] += 1
    else:
        donation = get_donation()
        donor_list[str_donor] = [donation, 1]

    create_letter(str_donor, donation)
    return_to_home_menu()


def get_donation():
    """ Prompt user for amount of donation """

    print()
    print("Please enter a donation amount or 'quit':")
    print()

    donation = (input("> "))
    if donation.lower() == 'quit':
        return home_menu()
    else:
        donation = is_float(donation)
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
    """ This will create a letter to display to the user showcasing both
        the donor and the donation amount

    """

    donation = str('%.2f' % donation)

    d = {'name': str_donor, 'donation': donation}

    print("""
    Dear {name},

    Thank you for your donation of {donation}. We here at Posters Without
    Borders greatly appreciate it. Your money will go towards ending the
    worldwide epidemic of posters on walls without frames.

    Thanks again,

    Kyle Winckler

    Director, F.H.W.
    """.format(**d))


def return_to_home_menu():
    """ This function will return you to the main menu at the end of either
        path.

    """

    print()
    print("Press Enter to Continue...")
    print()

    x = input('> ')
    if x == "":
        return home_menu()
    else:
        print("INVALID INPUT")


def create_report(donor_list):
    """Prints a list of donors, sorted by total donation amount"""

    sorted_list = sorted(donor_list.items(), key=operator.itemgetter(1),
                         reverse=True)

    print()
    print('     Name     |     Total    | # | Average ')
    print('______________________________________________')
    for i in range(len(sorted_list)):
        total = ('$%.2f' % sorted_list[i][1][0])
        average = (sorted_list[i][1][0]) / (sorted_list[i][1][1])
        average = str('$%.2f' % average)
        line = "{}\t| {}\t| {} | {}".format(sorted_list[i][0], total,
                                            sorted_list[i][1][1], average)
        print(line)

    return_to_home_menu()


def name_list():
    """ Creates and returns a list of names from the donor list """

    name_list = []
    for key in donor_list:
            name_list.append(key)
    return name_list


if __name__ == '__main__':

    not_done = True

    donor_list = {
        "Neal Stephenson": [2000, 3],
        "Luigi Mario": [1200, 1],
        "Ellie Arroway": [1700, 2],
        "Kevin Flynn": [1100, 2],
        "Severus Snape": [1000, 1]
    }

    while not_done:
        not_done = home_menu()
