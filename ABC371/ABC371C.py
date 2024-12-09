from itertools import permutations

N = int(input())

# グラフを隣接行列で管理
G = [[0] * N for _ in range(N)]
H = [[0] * N for _ in range(N)]

MG = int(input())
for _ in range(MG):
    u, v = map(int, input().split())
    G[u - 1][v - 1] = G[v - 1][u - 1] = 1

MH = int(input())
for _ in range(MH):
    a, b = map(int, input().split())
    H[a - 1][b - 1] = H[b - 1][a - 1] = 1

# コスト
A = []
for i in range(N - 1):
    row = list(map(int, input().split()))
    A.append([0] * (i + 1) + row)

ans = 1 << 60
for p in permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            # p[i],p[j]とi,jの関係(接続しているかどうか)が一致しないとコストがかかる
            if G[p[i]][p[j]] ^ H[i][j]:
                cost += A[i][j]
    ans = min(ans, cost)

print(ans)
