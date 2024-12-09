def flip(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()


S = input()
Q = int(input())
K = list(map(int, input().split()))

res = []
for k in K:
    k -= 1
    q = k // len(S)
    r = k % len(S)

    num = 0
    for i in range(61):
        if q & (1 << i):
            num += 1
    if num % 2 == 0:
        res.append(S[r])
    else:
        res.append(flip(S[r]))

print(*res)
