global size 
size = 50       # Size of menu border


def get_input():
    show_option("")     # insert new line between menu options and input
    s = input("| INPUT: ")
    len_string = len(s)
    padding = size - len_string - 1
    s = s + padding*" " + "|"
    return s

def main_menu():
    print_border(size)
    print("")

# Enclose the menu in terminal
def show_option(option):
    option = "|     " + option
    len_string = len(option)
    padding = size - len_string - 1
    option = option + padding*" " + "|"
    print(option)


def print_border(x):
    print(size*"=")



print_border(size)
show_option("(1) Search")
show_option("(2) Show all tables")
show_option("(3) Settings")
print(get_input())
