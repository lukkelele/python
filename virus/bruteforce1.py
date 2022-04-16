

class Doorknock:

    def __init__(self, n):
        self.n = n

    def get_chars(self):
        self.chars = [chr(i) for i in range(33, 127)]
        self.chars.remove('\\')
        print(self.chars)




D = Doorknock(4)
D.get_chars()
