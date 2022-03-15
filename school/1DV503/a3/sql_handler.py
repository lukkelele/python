# SQL queries

user_attr = """user_id int,
                f_name varchar(12),
                l_name varchar(20),
                gender varchar(10),
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


def get_attributes(entity):
    entity = entity.lower() 
    if entity == "librarian": return librarian_attr
    if entity == "book":      return book_attr


def create_table(name, attributes):
    query = f"""
    CREATE TABLE {name} (
        {attributes}
    );
    """
    return query


def insert_to_table(name, value):
    query = f"INSERT INTO {name} VALUES({value});"
    return query
