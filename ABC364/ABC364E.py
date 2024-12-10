# N個の料理
# 甘さA[i] しょっぱさB[i]
# 好きな順に食べて甘さ合計がX or しょっぱさ合計がYを超えたら終了
# 最大で何個食べられるか
N, X, Y = map(int, input().split())
INF = 1 << 60

# 甘さかしょっぱさのどちらかをDPの値にする
# DPの添え字は食べた料理の数

DP = [[[INF] * (X + 1) for j in range(i + 1)] for i in range(N + 1)]
DP[0][0][0] = 0

for i in range(N):
    A, B = map(int, input().split())
    for j in range(i + 1):
        for k in range(X + 1):
            DP[i + 1][j][k] = min(DP[i + 1][j][k], DP[i][j][k])
            if k + A <= X:
                DP[i + 1][j + 1][k + A] = min(DP[i + 1][j + 1][k + A], DP[i][j][k] + B)

# print(DP)

for j in range(N - 1, -1, -1):
    for k in range(X + 1):
        if DP[N][j][k] <= Y:
            print(j + 1)
            exit()
