N = int(input())
S = []
M = 0

for _ in range(N):
    s = list(input())
    S.append(s)
    M = max(M, len(s))

S2 = []
for s in S:
    S2.append(s + ["*"] * (M - len(s)))

T = list(zip(*S2[::-1]))

for t in T:
    tmp = list(t)
    while tmp[-1] == "*":
        tmp.pop()
    print("".join(tmp))
