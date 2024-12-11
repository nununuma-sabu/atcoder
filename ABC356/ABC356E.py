N = int(input())
A = list(map(int, input().split()))

# 10**6が最大値となりうる値
M = 10**6
cnt = [0] * (M + 1)

# 各数字の出現回数を覚えておく(累積和化)
for a in A:
    cnt[a] += 1

for i in range(M):
    cnt[i + 1] += cnt[i]

ans = 0
for c in range(1, M + 1):
    d = cnt[c] - cnt[c - 1]
    for kc in range(c, M + 1, c):
        k = kc // c
        ans += k * (cnt[min(10**6, kc + c - 1)] - cnt[kc - 1]) * d
    ans -= d * (d + 1) // 2

print(ans)
