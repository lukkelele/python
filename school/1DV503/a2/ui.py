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
    # If the search is a string that contains letters, proceed
    if search.isacii():
        search = search.lower() # Lowercase to reduce risk of errors within function
        detail = detail.lower()  
        if search == "planet" or search == "specie":
            columns = lib.get_column_names(search)  # Get all column names for the desired entity
            search = search.capitalize()    # Column names all begin with an uppercase letter
            for column_name in columns:     
                # Loop through the columns to see if the attribute that was
                # entered by the user is found within one of the column names
                if re.search(detail, column_name):
                    # When a match is found, sort out what type of entity the initial search
                    # was for and then return a string with the correct query to execute.
                    if search[0] == "P":    # if search == planet
                        primary_key = "p_name"
                    elif search[0] == "S":
                        primary_key = "s_name"
                    return f"SELECT {primary_key}, {column_name} FROM {search};"
        else:
            print("No information can be found by your search, check your spelling and try again!\n")
            return ""
    else:
        print("Make sure that the input provided doesn't contain digits or symbols.")
        return ""
