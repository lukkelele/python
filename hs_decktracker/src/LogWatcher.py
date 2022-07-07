# Used for reading output logs of gameplay
from datetime import datetime
import GameHandler
import subprocess
import linecache
import os
import re


class LogWatcher:

    def __init__(self, path, gameHandler):
        self._cached_stamp = 0
        self.blacklist = []
        self.path = path
        self.setup_attr()
        self.linecount = self.get_linecount(self.path)
        self.gameHandler = gameHandler

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

    def handle_event(self, line):
        match = re.search('zone=(PLAY|HAND|DECK|SECRET)', line)
        if match != None:
            self.gameHandler.evaluate(line)

    def getGameStart(self, logfile):
        linecount = 1
        try:
            with open(logfile) as file:
                for line in file:
                    game_start = re.search('Gameplay.Awake()', line)
                    if game_start != None and linecount not in self.blacklist:
                        self.blacklist.append(linecount)    # keep track of used linecounts
                        return linecount 
                    linecount += 1
        except: 
            print('Couldnt get gamestart')
        return None
