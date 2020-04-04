
QUIT = ""
YES = "Y"
DEFAULT_ACCEPT = ""


def main():
    email_to_name = {}
    user_email = input("Please enter a email to store:\n")
    while user_email != QUIT:
        name = get_name_from_email(user_email)
        conformation = input("Is {} your name? (Y/N)\n".format(name)).upper()
        if conformation != YES and conformation != DEFAULT_ACCEPT:
            name = input("Please enter name:\n")
        email_to_name[user_email] = name

        user_email = input("Please enter a email to store:\n")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(user_email):
    prefix = user_email.split("@")[0]
    name_parts = prefix.split(".")
    name = " ".join(name_parts).title()
    return name


main()
