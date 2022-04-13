



class Printer:

    def __init__(self, path):
        self.path = path
        self.r = open(self.path)
        self.text = self.separate_text()
        self.default_order = 0
        self.queue = []
        self.non_priority = []

    def separate_text(self):
        txt = ""
        for line in self.r:
            txt += line 
        return txt.split('$')

    def parse_text(self):
        for part in self.text:
            if part.startswith(':'):
                queue_spot = part[1]
                self.queue.append([queue_spot, part])
            else:
                if part != "":
                    self.non_priority.append([self.default_order, part])
                    self.default_order += 1
        priority_order = len(self.queue)
        non_priority_order = len(self.non_priority)
        print(f"Priority len: {priority_order}\nnon-priority: {non_priority_order}")






p = Printer('./muddy_sea.txt')
p.parse_text()
