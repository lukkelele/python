# SQL queries

# Data
# ----
# User
user_data1= '(1, "Lukas", "Gunnarsson", "male", "lg222xf@student.lnu.se", "0707385418", "Fabriksgatan 13A")'
user_data2 = '(2, "Migge", "Holm", "male", "migge_rickross@gmail.com", "0723941234", "Bakarvägen 22")'
user_data = user_data1 + "," + user_data2
# Author
author_data1 = '(1, "JK", "Rowling")'
author_data2 = '(2, "Stan", "Lee")'
author_data3 = '(3, "Stephen", "King")'
author_data = ",".join([author_data1, author_data2, author_data3])
# Librarian
librarian_data1 = '(1, "Tommy", "Green", "male", "0708312182", "Los Santos Boulevard 9")'
librarian_data2 = '(2, "Ellen", "Dorito", "female", "0773813209", "Rainbow Road 7")'
librarian_data2 = '(3, "Monty", "Python", "male", "0873018467", "Silicon Valley 2")'
librarian_data = ",".join([librarian_data1, librarian_data2])
# Library
library_data1 = '(5, "Bibblan", "Downtown road 5", "Kalimdor", 52451, "Coop")'
library_data2 = '(14, "Lib-town", "Eastern 52", "Outlands", 21451, "ICA")'
library_data = ",".join([librarian_data1, librarian_data2])
# Book
book_data1 = '(23, "Harry Potter and the Chamber of Secrets", "Fantasy", 200, 1)' # author_id == JK Rowling
book_data2 = '(19, "Harry Potter and the Prisoner of Azkaban", "Fantasy", 200, 1)' # author_id == JK Rowling
book_data3 = '(310, "Yatzy Rules", "Manual", 40, NULL)' 
book_data4 = '(212, "Poker guide for newbies", "Manual", 45, NULL)' 
book_data = ",".join([book_data1, book_data2, book_data3, book_data4])

user_attr = """user_id int,
                f_name varchar(12),
                l_name varchar(20),
                gender varchar(10),
                email varchar(40),
                phone int,
                address varchar(30),
                PRIMARY KEY (user_id)"""

librarian_attr = """emp_id int,
                    f_name varchar(12),
                    l_name varchar(20),
                    gender varchar(10),
                    phone int,
                    address varchar(30),
                    PRIMARY KEY (emp_id)"""

book_attr = """isbn int, 
               title varchar(45),
               genre varchar(20),
               price int,
               author_id int,
               PRIMARY KEY (isbn)"""

library_attr = """lib_id int,
                  lib_name varchar(18),
                  address varchar(20),
                  city varchar(16),
                  zipcode int,
                  company varchar(20),
                  PRIMARY KEY (lib_id)"""

author_attr = """author_id int,
                 f_name varchar(12),
                 l_name varchar(20),
                 PRIMARY KEY (author_id)"""

# Fix references..
has_published_attr = """author_id int,
                        isbn int,
                        publisher varchar(20),
                        publish_date date,
                        PRIMARY KEY (author_id, isbn),
                        FOREIGN KEY author_key (author_id) REFERENCES Author(author_id),
                        FOREIGN KEY isbn_key (isbn) REFERENCES Book(isbn)"""

loans_attr = """user_id int,
                isbn int,
                issued date,
                due_date date,
                PRIMARY KEY (user_id, isbn)"""

works_at_attr = """emp_id int,
                   lib_id int,
                   hire_date date,
                   PRIMARY KEY (emp_id, lib_id)"""



def get_data(entity):
    entity = entity.lower()
    if entity == "user": return user_data
    elif entity == "librarian": return librarian_data
    elif entity == "author": return author_data
    elif entity == "book":   return book_data


def get_attributes(entity):
    entity = entity.lower() 
    if   entity == "librarian": return librarian_attr
    elif entity == "book":      return book_attr
    elif entity == "user":      return user_attr
    elif entity == "library":   return library_attr
    elif entity == "author":    return author_attr
    elif entity == "has_published": return has_published_attr
    elif entity == "loans":     return loans_attr
    elif entity == "works_at":  return works_at_attr
    else:
        print("Nothing to return..")
        return ""


def create_table(name, attributes):
    query = f"""
    CREATE TABLE {name} (
        {attributes}
    );
    """
    return query


def insert_to_table(name, value):
    query = f"INSERT INTO {name} VALUES{value};"
    print(query)
    return query
