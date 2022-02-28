import mysql.connector


DB_NAME = "GUNNARSSON"
end_statement = "\n);"

def create_table(table_name, attributes):
    len_attributes = len(attributes)
    query = f"CREATE TABLE {table_name} (\n"
    for attribute in attributes:
        name = attribute[0]
        attr_type = attribute[1]
        if attributes.index(attribute) == (len_attributes - 1):     # if last attribute, dont add a ','
            query += name + " " + attr_type + end_statement
            break
        query += name + " " + attr_type + ",\n"
    return query 


attributes = [["PersonID", "int"], ["FirstName", "varChar(255)"], ["LastName", "varchar(255)"]]

s = create_table("Person", attributes)
