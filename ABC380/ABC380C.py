"""
0,1のみからなる長さNの文字列S
Sの中で先頭からK番目の1の塊をK-1番目の1の塊の直後まで移動した文字列を出力
"""

N, K = map(int, input().split())

# 番兵を仕込む
S = "0" + input() + "0"

# l:1の塊の左端 r:1の塊の右端
l = [-1]
r = [-1]

for i in range(1, N + 1):
    if S[i] == "1":
        if S[i - 1] == "0":
            l.append(i)
        if S[i + 1] == "0":
            r.append(i)

T = list(S)

for i in range(r[K - 1] + 1, r[K - 1] + r[K] - l[K] + 2):
    T[i] = "1"
for i in range(r[K - 1] + r[K] - l[K] + 2, r[K] + 1):
    T[i] = "0"

print("".join(T[1:-1]))
