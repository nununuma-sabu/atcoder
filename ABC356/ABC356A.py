from collections import deque

N, L, R = map(int, input().split())

B = deque()
for i in range(L, R + 1):
    B.append(i)

ans = []
for i in range(1, N + 1):
    if L <= i <= R:
        tmp = B.pop()
        ans.append(tmp)
    else:
        ans.append(i)

print(*ans)
