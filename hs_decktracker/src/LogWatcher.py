# Used for reading output logs of gameplay
from datetime import datetime
import subprocess
import linecache
import os
import re


class Logwatcher:

    def __init__(self, path):
        self._cached_stamp = 0
        self.path = path
        self.linecount = self.get_linecount(self.path)
        self.setup_attr()

    def setup_attr(self):
        attributes = ["entityName", "id", "zone", "zonePos", "cardId", "player"]
        for attr in attributes:
            len_attr = len(attr)
            attr = f"len_{attr}"
            setattr(self, attr, len_attr)

    def check_file(self):
        lines = self.get_linecount(self.path)
        if lines - self.linecount > 0: # change has occured
            d = lines - self.linecount
            k = 0
            f = open(self.path)
            file = f.readlines()
            print(f"New lines added to log: {d}")
            while k < d:
                line = file[self.linecount + k]
                self.handle_event(line)
                k += 1
            print("Exiting..")
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
    def handle_event(self, event):
        #match = re.search('zone=(PLAY|HAND|DECK|SECRET)', event)
        match = re.search('TRANSITIONING', event)
        if match != None:
            player_match = re.search('player=', event)
            player_idx = player_match.end()
            player = event[player_idx]  # determines if this is player 1 or 2
            cardId_match = re.search('cardId=', event)
            cardId_idx = cardId_match.end()
            cardId = event[cardId_idx:]
            if cardId != " ":
                cardId = cardId.split(' ', 1)[0]  # determines the cardId
            elif cardId == " ":
                cardId = "UNKNOWN ENTITY"
            

l = Logwatcher("../test/log_test.txt")
print(l.linecount)
while True:
    l.check_file()
