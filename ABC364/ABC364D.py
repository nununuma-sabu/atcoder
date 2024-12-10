from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# Aの中でbとk番目に近い点の距離を求めよ
# →距離d内に点はk個以上あるか

for _ in range(Q):
    b, k = map(int, input().split())
    low = -1
    high = 1 << 60
    while low + 1 < high:
        mid = (low + high) // 2
        c = bisect_right(A, b + mid) - bisect_left(A, b - mid)
        if c >= k:
            high = mid
        else:
            low = mid
    print(high)
