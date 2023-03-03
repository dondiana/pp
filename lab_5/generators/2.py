class even():
    def __init__ (self, n):
        self.end = n
        self.current = 0
    def __iter__ (self):
        return self
    def __next__(self):
        if(self.current > self.end):
            raise StopIteration()
        else:
            if(self.current %2 == 0):
                b = self.current
                self.current +=2
                return b
n = int(input())
print(*even(n), sep=', ')