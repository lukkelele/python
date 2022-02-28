import mysql.connector


DB_NAME = "GUNNARSSON"
end_statement = "\n);"


def create_database(db_name):
    query = f"CREATE DATABASE {db_name}"
    return query


def create_table(table_name, attributes):
    len_attributes = len(attributes)
    query = f"CREATE TABLE {table_name} (\n"
    for attribute in attributes:
        name = attribute[0]
        attr_type = attribute[1]
        constraint = ""
        if len(attribute) > 2:
            constraint = attribute[2]
        
        if attributes.index(attribute) == (len_attributes - 1):     # if last attribute, dont add a ','
            #query += name + " " + attr_type + " " + constraint + end_statement
            query += f"{name} {attr_type} {constraint} {end_statement}"
            break
        else:
            query += f"{name} {attr_type} {constraint},\n"
    return query 


# s_attr ==> string attribute instead of a list
def alter_table(table_name, method, s_attr):
    approved_methods = ["ADD", "DROP"]
    for approved_method in approved_methods:
        if method == approved_method:
            query = f"ALTER TABLE {table_name}\n{method} {s_attr} {end_statement}"
            return query
        else:
            return ""







# Tests

attributes = [["PersonID", "int"], ["FirstName", "varChar(255)", "NOT NULL"], ["LastName", "varchar(255)"]]

s = create_table("Person", attributes)
print(s)
