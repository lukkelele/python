# SQL queries

# Data
# ----
# USER
user_data1= '(1, "Lukas", "Gunnarsson", "male", "lg222xf@student.lnu.se", "0707385418", "Fabriksgatan 13A")'
user_data2 = '(2, "Migge", "Holm", "male", "migge_rickross@gmail.com", "0723941234", "Bakarvägen 22")'
user_data = user_data1 + "," + user_data2
# AUTHOR
author_data1 = '(1, "JK", "Rowling")'
author_data2 = '(2, "Stan", "Lee")'
author_data3 = '(3, "Stephen", "King")'
author_data = ",".join([author_data1, author_data2, author_data3])


user_attr = """user_id int,
                f_name varchar(12),
                l_name varchar(20),
                gender varchar(10),
                email varchar(32),
                phone int,
                address varchar(20),
                PRIMARY KEY (user_id)"""

librarian_attr = """emp_id int,
                    f_name varchar(12),
                    l_name varchar(20),
                    gender varchar(10),
                    phone int,
                    address varchar(20),
                    PRIMARY KEY (emp_id)"""

book_attr = """isbn int, 
               title varchar(16),
               genre varchar(12),
               price int,
               publication int, 
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
