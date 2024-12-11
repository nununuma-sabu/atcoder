# AND:二進法で書いて両方1のビットは1 他は0
N, M = map(int, input().split())
# N,Mは最大60ビット
L = 60
MOD = 998244353

ans = 0
for i in range(L):
    if (1 << i) & M:
        cycle = (N + 1) // (1 << (i + 1))
        amari = (N + 1) % (1 << (i + 1))
        # print(cycle, amari)
        ans += (cycle << i) + max(0, amari - (1 << i))

print(ans % MOD)
