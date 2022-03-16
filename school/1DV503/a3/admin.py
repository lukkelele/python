import mysql.connector as mysql
import sql_handler as query


class Admin:

    def __init__(self, user, passwd, url, db_name):
        self.user = user
        self.passwd = passwd
        self.url = url
        self.db_name = db_name
        self.connection_flag = False
    
    # Connect to database with passed parameters.
    # If passed database name isn't valid, connect without one specified.
    def connect_database(self):
        try:
            print(f"Connecting to {self.db_name} as {self.user} at {self.url}..")
            db = mysql.connect(
                    host=self.url,
                    user=self.user,
                    passwd=self.passwd,
                    database=self.db_name
                    )
            self.connection_flag = True
            print("Connected!")
        except:
            print(f"Connection to {self.db_name} could not be established..")
            db = mysql.connect(
                    host=self.url,
                    user=self.user,
                    passwd=self.passwd
                    )
            print(f"Connected without database specified.\nCredentials:\nuser: {self.user}\nurl: {self.url}")
        return db


    # Start the database.
    def start(self):
        self.db = self.connect_database()
        self.cursor = self.db.cursor()


    # Method to check database existance.
    # If no database is found, create a new one.
    def check_database_existance(self):
        if self.connection_flag == False:
            self.cursor.execute("create database library_db;")
            self.cursor.execute("use library_db;")
            self.db.commit()
            # Create tables
            self.initialize_db()
        else:
            print("Database exists!")
            try:
                self.cursor.execute("use library_db;")
                self.db.commit()
            except: # if error raised then database already selected
                pass

    # Create all tables and insert data.
    def initialize_db(self):    # Hard coded data
        self.cursor.execute(query.create_table("Librarian", query.get_attributes("Librarian")))
        self.cursor.execute(query.create_table("Library", query.get_attributes("Library")))
        self.cursor.execute(query.create_table("User", query.get_attributes("User")))
        self.cursor.execute(query.create_table("Author", query.get_attributes("Author")))
        self.cursor.execute(query.create_table("Book", query.get_attributes("Book")))
        self.cursor.execute(query.create_table("loans", query.get_attributes("loans")))
        self.db.commit()
        print("Tables created!")
        self.cursor.execute(query.add_FK("loans", "User", "user_id"))
        print("Foreign key added to loans --> User(user_id)")
        self.cursor.execute(query.add_FK("Book", "Author", "author_id"))
        print("Foreign key added to Book --> Author(author_id)")
        self.insert_data()      # add data
        

    # Gets all employees via a view to create a virtual table without
    # sensitive information about employees.
    def get_employees(self):
        self.cursor.execute(query.employee_view())
        self.db.commit()
        self.cursor.execute(query.get_employees())
        for employee in self.cursor:
            print(employee)


    # Method to insert data into the database
    def insert_data(self):
        tables = ["User", "Librarian", "Library", "Author", "Book", "loans"]
        for table in tables:
            print(f"Current table: {table}")
            table_data = query.get_data(table)
            #print(f"Current data: {table_data}")
            if table_data == None:
                pass
            else:
                self.cursor.execute(query.insert_to_table(table, query.get_data(table)))
        self.db.commit()
        print("Data inserted.")

    # Search a book in the database
    def search_book(self, booktitle):
        booktitle = booktitle.lower().capitalize()
        self.cursor.execute(f"SELECT title FROM Book WHERE title=\"{booktitle}\";")
        for book in self.cursor:
            print(book)

    # Displays all tables in the database
    def show_tables(self):
        self.cursor.execute("show tables;")
        print("\n====================================\n| TABLES:")
        for table in self.cursor:
            print("| "+str(table)[2:-3])
        print("====================================\n")

    # Displays all users that also are employed in the library
    def get_employed_users(self):
        self.cursor.execute(query.get_users_employed())
        print("\n====================================\n| EMPLOYED USERS:")
        for employed_user in self.cursor:
            print("| "+str(employed_user)[2:-2])
        print("====================================\n")

    # Displays all books within the 'Book' entity
    def show_books(self):
        self.cursor.execute(query.get_all_books())
        print("\n====================================\n| ALL BOOKS:")
        for result in self.cursor:
            print(str(result)[2:-2])
        print("====================================\n")

    # Checks the passed isbn if any books with the same isbn are available 
    def check_status(self, isbn):
        borrowed_books = 0
        self.cursor.execute(query.book_status(isbn))
        print("\n====================================\n| BOOK STATUS:")
        for result in self.cursor:  # if borrowed, count the amount
            borrowed_books += 1
        self.cursor.execute(query.count_books(isbn))
        for count in self.cursor:
            count = (int) (str(count)[1:-2])
            if borrowed_books < count:
                print("Book available")
                print("====================================\n")
                return False
            else:
                print("The book is not available.")
                print("====================================\n")
                return True

    # Get the average salary of all employees
    def get_avg_salary(self):
        self.cursor.execute(query.get_avg_salary())
        print("\n====================================\n| AVERAGE SALARY:")
        for result in self.cursor:  # if borrowed, count the amount
            print(str(result)[10:-4])
        print("====================================\n")

    # Display all borrowed booys
    def get_borrowed_books(self):
        self.cursor.execute(query.get_users_loaned())
        print("\n====================================\n| BOOKS OUT ON LOAN:")
        for result in self.cursor:  # if borrowed, count the amount
            print(str(result)[2:-2])
        print("====================================\n")

    # Display all genres and count them
    def display_genres(self):
        self.cursor.execute(query.get_amount_genres())
        print("\n====================================\n| GENRES:")
        for result in self.cursor:  # if borrowed, count the amount
            print(str(result)[2:-1])
        print("====================================\n")

    
    def avg_price_borrowed(self):
        self.cursor.execute(query.avg_price_borrowed_books())
        print("\n====================================\n| AVG PRICE ON LOANED BOOK:")
        for result in self.cursor:  # if borrowed, count the amount
            print(str(result)[10:-4])
        print("====================================\n")





