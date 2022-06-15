# Used for reading output logs of gameplay
from datetime import datetime
import subprocess
import linecache
import os
import re


class Logwatcher:

    def __init__(self, path):
        self._cached_stamp = 0
        self.logfile = self.open_log(path)
        self.file = path
        self.linecount = self.get_linecount()

    def open_log(self, path):
        log = open(f"{path}", 'r')
        return log

    def read_log(self, file):
        for line in file:
            match = re.search("zone=PLAY", line)
            if match is not None:
                print(line, end="\n")

    def poll(self):
        stamp = os.stat(self.file).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            linecount = self.get_linecount()
            # File changed, iterate through new lines 
            k = 0
            d = linecount - self.linecount   # new - old
            while k < d:
                line = self.logfile[self.linecount + k] # Newly added line in logfile
                # Parse new lines to see what kind of information they contain
            self.linecount = linecount # Update the linecount

    def get_linecount(self):
        p = subprocess.Popen(['wc', '-l', self.file], stdout=subprocess.PIPE,
                                                      stderr=subprocess.PIPE)
        result, err = p.communicate()
        if p.returncode != 0:
            raise IOError(err)
        return int(result.strip().split()[0])

    # Handle a line from the logfile
    def handle_event(self, event):
        # Different events: PLAY, HAND, DECK, SECRET
        match = re.search('zone=(PLAY|HAND|DECK|SECRET)', event)
        print(match)
        if match: print(event)


l = Logwatcher("../test/log_test.txt")
print(l.linecount)
r = l.logfile.readlines()
l.handle_event(r[1163])
