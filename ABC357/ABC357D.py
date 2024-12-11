# 初項と項数
N = int(input())
MOD = 998244353
# 公比
r = pow(10, len(str(N)), MOD)

ans = (N * (1 - pow(r, N, MOD)) * pow(1 - r, -1, MOD)) % MOD
print(ans)
