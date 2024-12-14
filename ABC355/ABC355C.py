N, T = map(int, input().split())
A = list(map(int, input().split()))

bingo = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        bingo[i][j] = i * N + j + 1

row = [0] * N
col = [0] * N

# 斜めはX,Yで管理
X, Y = 0, 0
ans = 0
for a in A:
    ans += 1
    i = (a - 1) // N
    j = (a - 1) % N
    row[i] += 1
    col[j] += 1
    if i == j:
        X += 1
    if i + j == N - 1:
        Y += 1
    if row[i] == N or col[j] == N or X == N or Y == N:
        print(ans)
        exit()

print(-1)
