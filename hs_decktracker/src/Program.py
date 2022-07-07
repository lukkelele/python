import GameHandler
import LogWatcher
import Entities

"""
Select deck by name , will later be with UI
At gamestart --> Load selected deck in to Player object
"""


class Program:

    def __init__(self):
        self.path = "../test/log_test.txt"
        self.logWatcher = LogWatcher.LogWatcher(self.path)

    def start(self):
        print('Starting program...\n')

        self.gameStart = self.logWatcher.getGameStart(self.path)
        if self.gameStart != None:
            while True:
                self.logWatcher.check_file(self.path)

        print('\nExiting program...')

    







P = Program()
P.start()
