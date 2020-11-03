class Song():
    def __init__(self):
        self.file = open('src/files/song.txt', '+r')
        self.f = self.file.read().splitlines()

    def read(self, n, m=0):
        try:
            if n <= 0 or m < 0:
                raise Exception("Values can't be lower than 1")

            if int(m) == 0:
                return(self.f[int(n)-1])
            else:
                if m-n <= 0:
                    raise Exception("First value can't be higher than the second")

                return(self.f[int(n)-1: int(m)])
        except:
            raise Exception('ValueError')
        

    def full(self):
        return(self.f)

    def close(self):
        self.file.close()