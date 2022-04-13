



class Printer:

    def __init__(self, path):
        self.path = path
        self.r = open(self.path)
        self.text = self.separate_text()

    def separate_text(self):
        txt = ""
        for line in self.r:
            txt += line 
        return txt.split('$')

    def parse_text(self):
        for part in self.text:
            print(part)


p = Printer('./muddy_sea.txt')
p.parse_text()
