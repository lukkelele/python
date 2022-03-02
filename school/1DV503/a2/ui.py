

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
