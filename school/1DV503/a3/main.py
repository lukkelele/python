import admin as a
import ui

# Login credentials
user = "root"
passwd = "root"
host = "localhost"
db_name = "library_db"

# Connect to database
db = a.Admin(user, passwd, host, db_name)
db.start()
db.check_database_existance()

# Loop the main menu until user wants to quit
user_input = '0' # to enter loop
while user_input != 'q':
    ui.main_menu()
    user_input = ui.get_input()
    
    if user_input == '1':
        ui.show_option(" Search for a book!")
        booksearch = ui.get_input()
        db.search_book(booksearch)
    elif user_input == '2':
        db.show_tables()
    elif user_input == '3':
        db.show_books()
    elif user_input == '4':
        isbn = ui.get_input()
        db.check_status(isbn)
    elif user_input == '5':
        db.get_employees()
    elif user_input == '6':
        db.get_employed_users()
    elif user_input == '7':
        db.avg_price_borrowed()
    elif user_input == '8':
        db.get_avg_salary()
    elif user_input == '9':
        db.get_borrowed_books()
    elif user_input == '10':
        db.display_genres()

