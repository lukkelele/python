# SQL queries



def create_table(name, attributes):
    query = f"""
    CREATE TABLE {name} (
        {attributes}
    );
    """
    return query
