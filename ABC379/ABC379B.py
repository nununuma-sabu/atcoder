from itertools import groupby

N, K = map(int, input().split())
S = input()

ans = 0
for k, g in groupby(S):
    if k == "X":
        continue
    ans += len(list(g)) // K

print(ans)
