import time

n = int(input())
s = int(input())

r = n**0.5

time.sleep(s/100)

print(f"Square root of {n} after {s} miliseconds is {r}")