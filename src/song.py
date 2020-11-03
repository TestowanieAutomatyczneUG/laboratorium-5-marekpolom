class Song():
    def __init__(self):
        self.file = open('src/files/song.txt', '+r')
        self.f = self.file.read().splitlines()

    def read(self, n, m=0):
        if m == 0:
            return(self.f[n-1])
        else:
            return(self.f[n-1: m])

    def close(self):
        self.file.close()