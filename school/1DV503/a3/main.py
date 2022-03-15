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
# loans(user_id, isbn, start_date, end_date)
# works_at(emp_id, lib_number, hire_date)
