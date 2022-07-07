import EventHandler
import LogWatcher
import Entities
import CardDB


class Program:


    def __init__(self):
        self.path = "../test/log_test.txt"
        self.eventHandler = EventHandler.EventHandler()
        self.logWatcher = LogWatcher.LogWatcher(self.path)


    def start(self):
        print('\nStarting program...\n')
        self.gameStart = self.eventHandler.getGameStart(self.path)
        while True:
            self.logWatcher.check_file(self.path)
        print('\nExiting program...')

    







P = Program()
P.start()
