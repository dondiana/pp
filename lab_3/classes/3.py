class shape():
    def __init__(p):
        pass
    def area(p, length, width):
        return 0

class rectangle(shape):
    def __init__(p, length = 0, width = 0):
        shape.__init__(p)
        p.length = length
        p.width = width

    def area(p):
        return p.length * p.width

l = int(input())
w = int(input())
r = rectangle(l, w)
print(r.area())

print(rectangle().area())