import admin as a

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

user = "root"
passwd = "root"
host = "localhost"
db_name = "library_db"



db = a.Admin(user, passwd, host, db_name)
db.start()
db.check_database_existance()

while True:
    print("Main Menu")
    user_input = input("Input: ")
    if user_input == '5':
        db.insert_data()
