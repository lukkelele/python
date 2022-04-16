

class Doorknock:

    def __init__(self, n):
        self.n = n

    def get_chars(self):
        self.chars = [chr(i) for i in range(47, 56)]
        #self.chars.remove('\\')

    def crack(self, n):
        passwd = []
        L = []
        for i in range(n):
            passwd.append(self.chars[0])
        for c in passwd:
            idx = passwd.index(c)
            print(f"CURRENT IDX: {idx}\nc: {c}")
            for x in range(len(self.chars)):
                for char in self.chars:
                    passwd[idx] = char
                    L.append(passwd)
                    print(passwd)
                passwd[idx+1] = self.chars[x]
        print(f"len(chars): {len(self.chars)}\n{len(self.chars)**2}\nlen(L): {len(L)}")


D = Doorknock(4)
D.get_chars()
D.crack(2)
