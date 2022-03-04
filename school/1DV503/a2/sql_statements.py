import mysql.connector
import csv

DB_NAME = "GUNNARSSON"
end_statement = "\n);"


def create_database(db_name):
    query = f"CREATE DATABASE {db_name}"
    return query


# [NAME, DATATYPE, CONSTRAINT, KEY PROPERTY]
def create_table(table, attributes):
    len_attributes = len(attributes)
    query = f"CREATE TABLE {table} (\n"
    for attribute in attributes:
        name = attribute[0]
        attr_type = attribute[1]
        constraint = ""
        key_property = ""
        if len(attribute) > 2:
            constraint = attribute[2]
            if len(attribute) > 3:                  # if primary key notation as an example
                key_property = attribute[3]
        if attributes.index(attribute) == (len_attributes - 1):     # if last attribute, dont add a ','
            #query += name + " " + attr_type + " " + constraint + end_statement
            query += f"{name} {attr_type} {constraint} {key_property} {end_statement}"
            break
        else:
            query += f"{name} {attr_type} {constraint} {key_property},\n"
    print(query)
    return query 


def copy_column(source_table, target_table, column, PK):
    query = f"""UPDATE {source_table}
                    SET {column} = (
                        SELECT {column}
                        FROM   {target_table}
                        WHERE  {source_table}.{PK} = {target_table}.{PK}
                );  """
    return query


def drop_column(table, column):
    query = f"ALTER TABLE {table} DROP COLUMN {column};"
    return query


def copy_table(source_table, target_table):
    query = f"INSERT INTO {target_table} SELECT * FROM {source_table};"
    return query


def duplicate_table(source_table, new_table):
    query = f"CREATE TABLE {new_table} LIKE {source_table};"
    return query


def check_data_exist(table):
    query = f"""SELECT COUNT(*)
                FROM (select top 1 *
                FROM TABLE) {table};
            """
    return query


def insert_into(table, values):
    query = f"""
            INSERT INTO {table}
            VALUES {values}
            """
    return query


def list_planets():
    query = f"""SELECT p_name
                FROM Planet
             """
    return query


def list_planet_details(table, user_input):
    query = f"""
            SELECT DISTINCT *
            FROM Planet AS p
            WHERE p.p_name={user_input}
             """
    return query


def search_species_height(min_height):
    query = f"""
            SELECT *
            FROM Specie AS s
            WHERE s.height > {min_height}
             """
    return query


# Estimated climate for a species ---> their homeworld
def estimated_climate(specie):
    query = f"""
            SELECT climate
            FROM Specie as s
            WHERE 
             """
    return query



