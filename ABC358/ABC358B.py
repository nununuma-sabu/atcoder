N, A = map(int, input().split())
T = list(map(int, input().split()))

# 前の人の購入完了時刻
pre = 0

for t in T:
    buy = max(t, pre) + A
    print(buy)
    pre = buy
