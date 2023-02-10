class Filter():
    def isPrime(p, n):
        if (n < 2):
            return False
        else:
            for i in range(2, n):
                if(n % i == 0):
                    return False
        return True   

    def filter(p, numbers):
        return filter(lambda x : p.isPrime(x), numbers)

primefilter = Filter()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime = list(primefilter.filter(a))
print(prime)
