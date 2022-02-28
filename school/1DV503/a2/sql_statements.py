import mysql.connector


DB_NAME = "GUNNARSSON"
end_statement = "\n);"

# Attributes is a list holding a list[2] with attribute name and type
def create_table(table_name, attributes):
    len_attributes = len(attributes)
    attr_string = ""
    query = f"CREATE TABLE {table_name} ("
    for attribute in attributes:
        if attributes.index(attribute) == (len_attributes - 1):     # if last attribute, dont add a ','
            query =+ name + " " + attr_type + end_statement
        name = attribute[0]
        attr_type = attribute[1]
        query =+ name + " " + attr_type + ","
        



cursor.execute()




try:
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database=DB_NAME
            )
except:     # if no database is recognized by DB_NAME
    db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root"
            )

cursor = db.cursor()
