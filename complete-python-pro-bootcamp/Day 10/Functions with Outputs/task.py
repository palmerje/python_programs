


def format_name(f_name, l_name):
    """Takes first name and last name and formats it
    to return title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name(input("What is your first name? "), input("What is your last name? "))
print(formatted_string)