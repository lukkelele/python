import lib
import re


def print_line(n):
    c = 0
    while c < n:
        print("=", end="")
        c += 1


def main_menu():
    print("\n")
    print_line(19)
    print(" MAIN MENU ", end="")
    print_line(19)
    print("\n")
    print("(1) LIST ALL PLANETS\n(2) SEARCH FOR PLANET DETAILS\n(3)"+
            " SEARCH FOR SPECIES ABOVE A CERTAIN HEIGHT\n"+
            "(4) GUESS THE DESIRED CLIMATE\n(5) SHOW AVERAGE LIFESPAN PER SPECIES CLASSIFICATION\n")
    print_line(50)
    print()


def search_details(search, detail):
    #columns = lib.get_column_names(search) # granted no input errors are included
    search = search.lower()
    detail = detail.lower()
    if search == "planet" or search == "specie":
        columns = lib.get_column_names(search)
        search = search.capitalize()
        for column_name in columns:
            if re.search(detail, column_name):
                print(f"Match found ==> {column_name}")
                if search[0] == "P":    # if search == planet
                    primary_key = "p_name"
                elif search[0] == "S":
                    primary_key = "s_name"
                return f"SELECT {primary_key}, {column_name} FROM {search};"
    else:
        print("No information can be found by your search, check your spelling and try again!\n")
        return ""
