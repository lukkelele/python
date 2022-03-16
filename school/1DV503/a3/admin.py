import mysql.connector as mysql
import sql_handler as query

# 1. At least 3 queries should query data from more than one table, i.e., you should use at
# least two multirelation queries
# 2. You should make use of SQL JOIN
# 3. You should make use of Aggregation and Grouping
# 4. Create and use a View

# Queries:
# See if a book is available
# Check employees at a particular library
# Check library details as a user --> create a view with sensitive information removed

class Admin:

    def __init__(self, user, passwd, url, db_name):
        self.user = user
        self.passwd = passwd
        self.url = url
        self.db_name = db_name
        self.connection_flag = False

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
    

    def start(self):
        self.db = self.connect_database()
        self.cursor = self.db.cursor()


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


    def initialize_db(self):    # Hard coded data
        self.cursor.execute(query.create_table("Librarian", query.get_attributes("Librarian")))
        self.cursor.execute(query.create_table("Library", query.get_attributes("Library")))
        self.cursor.execute(query.create_table("User", query.get_attributes("User")))
        self.cursor.execute(query.create_table("Author", query.get_attributes("Author")))
        self.cursor.execute(query.create_table("Book", query.get_attributes("Book")))
        self.cursor.execute(query.create_table("loans", query.get_attributes("loans")))
#        self.cursor.execute(query.create_table("stored_in", query.get_attributes("stored_in")))
        self.db.commit()
        print("Tables created!")
        self.cursor.execute(query.add_FK("loans", "User", "user_id"))
        print("Foreign key added to loans --> User(user_id)")
        self.cursor.execute(query.add_FK("Book", "Author", "author_id"))
        print("Foreign key added to Book --> Author(author_id)")
#        self.cursor.execute(query.add_FK("stored_in", "Book", "isbn"))
#        print("Foreign key added to stored_in --> Book(isbn)")
#        self.cursor.execute(query.add_FK("stored_in", "Library", "lib_id"))
#        print("Foreign key added to stored_in --> Library(lib_id)")
#        self.db.commit()
        self.insert_data()      # add data
        


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


    def search_book(self, booktitle):
        booktitle = booktitle.lower().capitalize()
        self.cursor.execute(f"select title from Book where title=\"{booktitle}\";")
        for book in self.cursor:
            print(book)


    def show_tables(self):
        self.cursor.execute("show tables;")
        print("\n====================================\n| TABLES:")
        for table in self.cursor:
            print("| "+str(table)[2:-3])
        print("====================================\n")


    def get_employed_users(self):
        self.cursor.execute(query.get_users_employed())
        print("\n====================================\n| EMPLOYED USERS:")
        for employed_user in self.cursor:
            print("| "+str(employed_user)[2:-3])
        print("====================================\n")


    def show_books(self):
        self.cursor.execute(query.get_all_books())
        print("\n====================================\n| ALL BOOKS:")
        for result in self.cursor:
            print(result)
        print("====================================\n")


    def check_status(self, isbn):
        borrowed_books = 0
        self.cursor.execute(query.book_status(isbn))
        print("\n====================================\n| BOOK STATUS:")
        for result in self.cursor:  # if borrowed, count the amount
            borrowed_books += 1
        self.cursor.execute(query.count_books(isbn))
        for count in self.cursor:
            print(str(count)[1:-2])
            count = (int) (str(count)[1:-2])
            if borrowed_books < count:
                print("Book available")
                return False
            else:
                print("The book is not available anywhere.")
                return True
        print("====================================\n")













