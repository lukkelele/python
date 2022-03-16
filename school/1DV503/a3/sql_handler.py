# SQL queries

# ========= HARD CODED DATA ===================================================================
# User(user_id, f_name, l_name, gender, email, phone, address)
user_data1 = '(1, "Lukas", "Gunnarsson", "male", "lg222xf@student.lnu.se", "0707385418", "Fabriksgatan 13A")'
user_data2 = '(12, "Migge", "Holm", "male", "migge_rickross@gmail.com", "0723941234", "Bakarvagen 22")'
user_data3 = '(54, "Ellen", "Dorito", "female", "dancing_dorito@hotmail.com", "0773813209", "Rainbow Road 7")'
user_data4 = '(30, "Bengt", "Eldorado", "male", "Bingo_Bengan@outlook.com", "0853538563", "Lyckogatan 21")'
user_data = ",".join([user_data1, user_data2, user_data3, user_data4])
# Author(author_id, f_name, l_name)
author_data1 = '(1, "JK", "Rowling")'
author_data2 = '(2, "Stan", "Lee")'
author_data3 = '(3, "Stephen", "King")'
author_data4 = '(6, "Lukas", "Gunnarsson")'
author_data = ",".join([author_data1, author_data2, author_data3, author_data4])
# Librarian(emp_id, f_name, l_name, gender, lib_id, salary, phone, address)
librarian_data1 = '(1, "Tommy", "Green", "male", 5, 62000, "0708312182", "Los Santos Boulevard 9")'
librarian_data2 = '(2, "Ellen", "Dorito", "female", 5, 50000,"0773813209", "Rainbow Road 7")'
librarian_data3 = '(3, "Monty", "Python", "male", 14, 44000, "0873018467", "Silicon Valley 2")'
librarian_data = ",".join([librarian_data1, librarian_data2, librarian_data3])
# Library(lib_id, lib_name, address, country, zipcode, company)
library_data1 = '(5, "Bibblan", "Downtown road 5", "Kalimdor", 52451, "Coop")'
#library_data2 = '(14, "Lib-town", "Eastern 52", "Outlands", 21451, "ICA")'
library_data = ",".join([library_data1])

# Book(isbn, title, genre, price, author_id, lib_id)
book_data1 = '(23, "Harry Potter and the Chamber of Secrets", "Fantasy", 200, 1, 5)' # author_id == JK Rowling
book_data2 = '(19, "Harry Potter and the Prisoner of Azkaban", "Fantasy", 200, 1, 5)' # author_id == JK Rowling
book_data2 = '(37, "SQL and its Crazy Rave Culture", "Comedy", 100, 6, 5)' 
book_data3 = '(310, "Yatzy Rules", "Manual", 40, NULL, 5)' 
book_data4 = '(212, "Poker guide for newbies", "Manual", 45, NULL, 5)' 
book_data = ",".join([book_data1, book_data2, book_data3, book_data4])
# Loans(user_id, isbn, issued, due_date)
loans_data1 = '(12, 310, "2022-04-20", "2022-05-20")'   # Migge --> Yatzy
loans_data2 = '(12, 212, "2022-04-22", "2022-05-22")'   # Migge --> Poker
loans_data3 = '(30,  19,  "2022-02-12", "2022-03-12")'   # Lukas --> Poker
loans_data4 = '(54,  37,  "2022-06-09", "2022-07-04")'
loans_data = ",".join([loans_data1, loans_data2, loans_data3, loans_data4])
# ========= DATA END ===========================================================================


user_attr =  """user_id int, f_name varchar(12), l_name varchar(20),
                gender varchar(10), email varchar(40), phone int,
                address varchar(30),
                PRIMARY KEY (user_id)"""

librarian_attr = """emp_id int, f_name varchar(12), l_name varchar(20),
                    gender varchar(10), lib_id int, salary int, phone int,
                    address varchar(30),
                    PRIMARY KEY (emp_id)"""

book_attr = """isbn int, title varchar(45), genre varchar(20),
               price int, author_id int, lib_id int,
               PRIMARY KEY (isbn)"""

library_attr = """lib_id int, lib_name varchar(18), address varchar(20),
                  city varchar(16), zipcode int, company varchar(20),
                  PRIMARY KEY (lib_id)"""

author_attr = """author_id int, f_name varchar(12), l_name varchar(20),
                 PRIMARY KEY (author_id)"""


loans_attr = """user_id int, isbn int, issued date, due_date date,
                PRIMARY KEY (user_id, isbn)"""



def employee_view():
    query = "CREATE VIEW employee_view AS SELECT f_name, l_name, gender FROM Librarian;"
    return query

def get_employees():
    query = "SELECT * FROM employee_view;"
    return query

def add_FK(table, target_table, key):
    query = f"{table} ADD FOREIGN KEY({key}) REFERENCES {target_table}({key});"
    return query

def get_amount_genres():
    query = "SELECT Book.genre, COUNT(*) FROM Book GROUP BY Book.genre HAVING COUNT(*) > 1;"
    return query

def get_users_loaned():
    query = "SELECT DISTINCT U.f_name, U.l_name from User as U, loans as L WHERE U.user_id=L.user_id;"
    return query

# Fetch the employees that are also registered as a "user"
def get_users_employed():
    query = f"""SELECT user_id, U.f_name, U.l_name
                FROM User AS U JOIN Librarian AS L
                ON L.f_name=U.f_name AND L.l_name=U.l_name AND L.address=U.address;
                """
    return query

# Salary only exists in Librarian therefore no parameters has to be passed to determine the table
def get_avg_salary():
    query = f"""SELECT AVG(salary) FROM Librarian;"""
    return query

def avg_price_borrowed_books():
    query = "SELECT AVG(Book.price) FROM Book, loans WHERE Book.isbn=loans.isbn;"
    return query

def get_all_books():
    query = "SELECT Book.title, Author.f_name, Author.l_name, Book.genre FROM Book JOIN Author ON Book.author_id=Author.author_id;"
    return query

def book_status(isbn):
    query = f"SELECT issued, due_date FROM loans WHERE isbn={isbn};"
    return query

def count_books(isbn):
    query = f"SELECT COUNT(*) from Book WHERE isbn={isbn};"
    return query

def get_data(entity):
    entity = entity.lower()
    if entity == "user": return user_data
    elif entity == "librarian": return librarian_data
    elif entity == "library":   return library_data
    elif entity == "author":    return author_data
    elif entity == "book":      return book_data
    elif entity == "loans":     return loans_data

def get_attributes(entity):
    entity = entity.lower() 
    if   entity == "librarian": return librarian_attr
    elif entity == "book":      return book_attr
    elif entity == "user":      return user_attr
    elif entity == "library":   return library_attr
    elif entity == "author":    return author_attr
    elif entity == "loans":     return loans_attr
    else:
        print("Nothing to return..")
        return ""


def create_table(name, attributes):
    query = f"CREATE TABLE {name} ({attributes});"
    return query


def insert_to_table(name, value):
    query = f"INSERT INTO {name} VALUES{value};"
    return query


