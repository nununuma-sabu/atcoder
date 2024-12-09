from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
INF = 1 << 60
d = [INF] * (N + 1)
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    if a == 1:
        d[b] = 1
        q.append(b)

while q:
    x = q.popleft()
    for y in G[x]:
        if d[y] > d[x] + 1:
            d[y] = d[x] + 1
            q.append(y)

if d[1] < INF:
    print(d[1])
else:
    print(-1)
