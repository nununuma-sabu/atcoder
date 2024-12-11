# A,B,?からなるN文字の文字列S
# Sの?をAもしくはBに変換した文字列を考える
# そのうち、長さKの回文を含まないものの個数を求める
from collections import defaultdict

N, K = map(int, input().split())
S = input()
MOD = 998244353
DP = [defaultdict(int) for _ in range(N + 1)]
DP[0][""] = 1


# 回文の確認
def check(S):
    return len(S) == K and S == S[::-1]


for i in range(N):
    for k, v in DP[i].items():
        for c in "AB":
            if S[i] in [c, "?"] and not check(k + c):
                nk = (k + c)[-(K - 1) :]
                # print(nk)
                DP[i + 1][nk] = (DP[i + 1][nk] + v) % MOD

print(sum(DP[N].values()) % MOD)
