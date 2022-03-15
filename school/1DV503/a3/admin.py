import mysql.connector as mysql
import sql_handler as query

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
        #self.db.autocommit()
        #print("Autocommit set to TRUE")
        self.cursor = self.db.cursor()
        self.cursor.execute("use library_db;")

    def check_database_existance(self):
        if self.connection_flag == False:
            print("Creating tables..")
            # Create all tables if no database
            self.cursor.execute(query.create_table("Librarian", query.get_attributes("Librarian")))


if __name__ == "__main__":
    admin = Admin("root", "root", "localhost", "library_db")
    admin.start()
    admin.check_database_existance()
    admin.cursor.execute(query.create_table("Librarian", query.get_attributes("Librarian")))
    admin.cursor.execute("insert into Librarian values (1, \"Lukas\", \"Gunnarsson\");")
    admin.db.commit()
    print("Exiting...")

