# SQL queries

librarian_attr = "emp_id int, f_name varchar(12), l_name varchar(20)"
book_attr = "isbn int, title varchar(16), genre varchar(12), price int, publication int"


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
