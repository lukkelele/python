import admin as a
import ui

# ---- Relation Schema ----
# ======================================================================
# User (user_id, f_name, l_name, gender, email, phone, address)
# Librarian (emp_id, f_name, l_name, gender, phone, address)
# Library (lib_id, lib_name, address, city, zipcode, country, company)
# Book (isbn, title, genre, price, publication)
# Author (author_id, f_name, l_name)
# 
# has_published(author_id, isbn)
# loans(user_id, isbn, issued, due_date, fine)
# works_at(emp_id, lib_number, hire_date)
#
#
# =====================================================================

# Query Ideas
# Select the authors names who's books are borrowed at the moment
# Select the price of books who are borrowed at the moment
# Select the names of users that are also employees if they have borrowed any books

user = "root"
passwd = "root"
host = "localhost"
db_name = "library_db"



db = a.Admin(user, passwd, host, db_name)
db.start()
db.check_database_existance()

while True:
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
    elif user_input == '8':
        db.get_employed_users()

    elif user_input == '10':
        db.insert_data()
