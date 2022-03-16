size = 50       # Size of menu border

def get_input():
    show_option("")     # insert new line between menu options and input
    s = input("| INPUT: ")
    len_string = len(s)
    padding = size - len_string - 1
    print_s = s + padding*" " + "|"
    print(print_s)
    return s

def main_menu():
    print_border(size)
    show_option("(1)  Search")
    show_option("(2)  Display all tables")
    show_option("(3)  Display all books")
    show_option("(4)  Check book status")
    show_option("(5)  Get employee information")
    show_option("(6)  Get employed users")
    show_option("(7)  Display average price of currently borrowed books")
    show_option("(8)  Display average salary of an employee")
    show_option("(9)  Show users that have borrowed books")
    show_option("(10) Display book genres and count them")
    print_border(size)

# Enclose the menu in terminal
def show_option(option):
    option = "|     " + option
    len_string = len(option)
    padding = size - len_string - 1
    option = option + padding*" " + "|"
    print(option)


def print_border(x):
    print(size*"=")


