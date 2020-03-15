# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message


MENU = "(H)ello\n" \
       "(G)oodbye\n" \
       "(Q)uit"


def main():

    name = input("Please enter your name\n")

    print(MENU)

    select_menu(name)

    print("You have quit, thanks for coming :)")


def select_menu(name):
    choice = input("Please enter what you would like to do\n").upper()
    while choice != "Q":
        if choice == "H":
            print("Hello {}".format(name))
        elif choice == "G":
            print("Goodbye {}".format(name))
        else:
            print("Invalid message")
        print(MENU)
        choice = input("Please enter what you would like to do\n").upper()


main()
