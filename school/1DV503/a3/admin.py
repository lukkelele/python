import mysql.connector as mysql


class Admin:

    def __init__(self, user, passwd, url, db_name):
        self.user = user
        self.passwd = passwd
        self.url = url
        self.db_name = db_name

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
            self.connection_flag = False
        return db


