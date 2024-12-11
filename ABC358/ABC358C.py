from collections import deque

N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 1 << 60

for i in range(1 << N):
    chk = [False] * M
    Q = deque()
    for j in range(N):
        if (1 << j) & i:
            Q.append(S[j])
    cnt = len(Q)
    while Q:
        tmp = Q.popleft()
        for k in range(M):
            if tmp[k] == "o":
                chk[k] = True
    if all(chk):
        ans = min(ans, cnt)

print(ans)
