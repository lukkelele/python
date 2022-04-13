



class Printer:

    def __init__(self, path):
        self.path = path
        self.r = open(self.path)
        
    def parse_text(self):
        for line in self.r:
            if line != "":
                print(line, end="")


p = Printer('./muddy_sea.txt')
p.parse_text()
