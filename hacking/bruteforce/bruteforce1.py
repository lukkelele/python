

class Doorknock:

    def __init__(self, n):
        self.n = n

    def get_chars(self):
        self.chars = [chr(i) for i in range(46, 50)]
        #self.chars.remove('\\')

    def crack(self, n):
        passwd = []
        L = []
        for i in range(n):
            passwd.append(self.chars[0])
        print(passwd)
        idx = 0
        for c in passwd:
            print(f"CURRENT IDX: {idx}\nc: {c}")
            for x in range(len(self.chars)):
                for char in self.chars:
                    passwd[idx] = char
                    L.append(passwd)
                    print(passwd)
                passwd[idx] = self.chars[x]
            idx += 1
        print(f"len(chars): {len(self.chars)}\n{len(self.chars)**2}\nlen(L): {len(L)}")


D = Doorknock(4)
D.get_chars()
D.crack(2)
