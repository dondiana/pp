class shape():
    def __init__(p) -> None:
        pass
    def area(p):
        return 0

class square(shape):
    def __init__(p, length = 0):
        shape.__init__(p)
        p.length = length
    
    def area(p):
        return p.length * p.length


x = int(input())
s = square(x)
print(s.area())
print(square().area())