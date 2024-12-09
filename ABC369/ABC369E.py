# N個の島がM本の橋で結ばれている
# 島1から島Nに行きたい
# ※途中でK本の橋を通りたい
# このときの最短移動距離は
# という質問をQ回解く

# Nが最大400なのでワーシャルフロイド
# 400**3 = 64000000
from itertools import permutations

N, M = map(int, input().split())
U = [0] * M
V = [0] * M
T = [0] * M
INF = 1 << 60

# 隣接行列
D = [[0 if i == j else INF for j in range(N)] for i in range(N)]
for i in range(M):
    U[i], V[i], T[i] = map(int, input().split())
    U[i] -= 1
    V[i] -= 1
    D[U[i]][V[i]] = D[V[i]][U[i]] = min(D[U[i]][V[i]], T[i])

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

# print(D)
Q = int(input())

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    for i in range(K):
        B[i] -= 1
    ans = INF
    for p in permutations(B):
        for mask in range(1 << K):
            cost = 0
            cur = 0
            for i in range(K):
                if mask >> i & 1:
                    cost += D[cur][U[p[i]]] + T[p[i]]
                    cur = V[p[i]]
                else:
                    cost += D[cur][V[p[i]]] + T[p[i]]
                    cur = U[p[i]]
            cost += D[cur][N - 1]
            ans = min(ans, cost)
    print(ans)
