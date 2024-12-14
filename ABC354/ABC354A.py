H = int(input())

i = 0
x = 0

while x <= H:
    x += 2**i
    i += 1

print(i)
