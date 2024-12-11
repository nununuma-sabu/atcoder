from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

D = defaultdict(list)

for i in range(N):
    D[A[i]].append(W[i])


ans = 0
for v in D.values():
    v.sort()
    cnt = len(v)
    if cnt > 1:
        ans += sum(v[:-1])

print(ans)
