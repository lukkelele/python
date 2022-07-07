# Used for reading output logs of gameplay
from datetime import datetime
import EventHandler
import subprocess
import linecache
import os
import re


class LogWatcher:

    def __init__(self, path):
        self._cached_stamp = 0
        self.path = path
        self.linecount = self.get_linecount(self.path)
        self.setup_attr()
        self.eventHandler = EventHandler.EventHandler()

    def setup_attr(self):
        attributes = ["entityName", "id", "zone", "zonePos", "cardId", "player"]
        for attr in attributes:
            len_attr = len(attr)
            attr = f"len_{attr}"
            setattr(self, attr, len_attr)

    def check_file(self, path):
        lines = self.get_linecount(path)
        if lines - self.linecount > 0: # change has occured
            diff = lines - self.linecount
            k = 0
            f = open(path)
            file = f.readlines()
            print(f"\nNew lines added to log: {diff}\n")
            while k < diff:
                line = file[self.linecount + k]
                self.handle_event(line)
                k += 1
            self.linecount = lines
            f.close()

    def get_linecount(self, file):
        p = subprocess.Popen(['wc', '-l', file], stdout=subprocess.PIPE,
                                                      stderr=subprocess.PIPE)
        result, err = p.communicate()
        if p.returncode != 0:
            raise IOError(err)
        return int(result.strip().split()[0])

    # Handle a line from the logfile
    def handle_event(self, line):
        match = re.search('zone=(PLAY|HAND|DECK|SECRET)', line)
        #match = re.search('TRANSITIONING', line)
        if match != None:
            self.eventHandler.evaluate(line)


#test_line = 'TRANSITIONING card [entityName=UNKNOWN ENTITY [cardType=INVALID] id=42 zone=HAND zonePos=0 cardId= player=2] to OPPOSING HAND'

#l = Logwatcher("../test/log_test.txt")
#print(l.linecount)
#l.handle_event(test_line)

#while True:
#    l.check_file()
