



class Printer:

    def __init__(self, path):
        self.path = path
        self.r = open(self.path)
        self.queue = []

    def parse_text(self):
        for line in self.r:
            if line.startswith("$:"):
                txt = ""
                lines = 0
                while self.r.readline() != "":
                    txt += self.r.readline()
                    lines += 1
                    print(line)


p = Printer('./muddy_sea.txt')
p.parse_text()
