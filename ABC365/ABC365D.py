# じゃんけんをN回した
# 相手の出した手は全て予知できる
# そのとき、一度も負けなかった かつ 連続して同じ手は出さなかった
# 最大何回勝ったか

N = int(input())
S = input()
INF = 1 << 60


# じゃんけんで勝ったかどうか
# 0:グー 1:パー 2:チョキを想定
def score(x, y):
    if (x - y) % 3 == 1:
        return 1
    elif x == y:
        return 0
    else:
        return -INF


DP = [[-INF] * 3 for _ in range(N + 1)]
DP[0][0] = 0
DP[0][1] = 0
DP[0][2] = 0

for i in range(N):
    y = {"R": 0, "P": 1, "S": 2}[S[i]]
    for j in range(3):
        for k in range(3):
            # 次に出す手kと今出した手jが異なる場合
            if k != j:
                DP[i + 1][k] = max(DP[i + 1][k], DP[i][j] + score(k, y))

print(max(DP[N]))
