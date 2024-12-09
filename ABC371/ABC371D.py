from bisect import bisect_left, bisect_right

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

# 村の人数の累積和
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + P[i]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    l = bisect_left(X, L)
    r = bisect_right(X, R)
    print(S[r] - S[l])
