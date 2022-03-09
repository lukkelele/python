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


def show_planet_details(search, planets):
    if search.isascii() == True:
        for planet in planets:
            if search.lower() == planet.lower():
                # if a search is equal to a planet name, proceed
                return f"SELECT * FROM Planet WHERE p_name=\"{search}\";"


# Wrong method implementation..
def search_details(search):
    # If the search is a string that contains letters, proceed
    if search.isascii() == True:
        s = "SELECT p_name, {} FROM {};"
        search = search.lower() # Lowercase to reduce risk of errors within function
        columns = lib.get_column_names("planet")  # Get all column names for the desired entity
        if search == "climate" or search == "terrain":
            if search == "climate":
                return s.format("climate", "Environment")
            elif search == "terrain":   # if statement instead of else if more entities are to get added in the future
                return s.format("terrain", "Terrain")
        for column_name in columns:     
            # Loop through the columns to see if the attribute that was
            # entered by the user is found within one of the column names
            if re.search(search, column_name):
                # When a match is found, sort out what type of entity the initial search
                # was for and then return a string with the correct query to execute.
                return f"SELECT p_name, {column_name} FROM Planet;"
        else:
            print("No information can be found by your search, check your spelling and try again!\n")
            return ""
    else:
        print("Make sure that the input provided doesn't contain digits or symbols.")
        return ""
