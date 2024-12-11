from bisect import bisect_right

# N匹の蟻 T秒間で蟻がすれ違う回数
N, T = map(int, input().split())
# S:蟻の向き 0:左 1:右
S = input()

# 蟻の座標
X = list(map(int, input().split()))

# 向きの違う蟻同士は1秒で距離が2ずつ縮む
# T秒なので現在地Xから2T先までの左向きの蟻の個数を数える
L = []
R = []
for i in range(N):
    if S[i] == "0":
        L.append(X[i])
    else:
        R.append(X[i])

L.sort()

ans = 0
for r in R:
    ans += bisect_right(L, r + 2 * T) - bisect_right(L, r)

# print(R)
# print(L)
print(ans)
