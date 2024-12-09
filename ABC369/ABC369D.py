N = int(input())
A = list(map(int, input().split()))
INF = 1 << 60

# DP[i][j]:i番目までのモンスターまででの最大獲得EXP
# j:0→経験値1倍 j:1→経験値2倍
DP = [[0, -INF] for _ in range(N + 1)]

for i in range(N):
    for j in range(2):
        # モンスターを倒さない
        DP[i + 1][j] = max(DP[i + 1][j], DP[i][j])
        # モンスターを倒す
        # ※ not 0 -> 1, not 1 -> 0と見なせる
        DP[i + 1][not j] = max(DP[i + 1][not j], DP[i][j] + A[i] * (j + 1))

print(max(DP[N]))
