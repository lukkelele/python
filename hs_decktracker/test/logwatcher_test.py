import sys
sys.path.append('../')
from src import logwatcher

path = "./log_test.txt"

def test():
    print(f"[TEST] Opening file at {path}")
    f = logwatcher.open_log(path)
    logwatcher.read_log(f)

test()
