""""
H行W列のマス目
あるマスに加湿器があり、マンハッタン距離がD以下のマスが加湿される
マスを2個選んで加湿するとき、加湿されるマスの最大個数を求める
"""

from itertools import combinations


def humid(h1, w1, h2, w2):
    ret = 0
    grid = [[False] * W for _ in range(H)]
    for dh in range(-D, D + 1):
        for dw in range(-D, D + 1):
            if abs(dh) + abs(dw) > D:
                continue
            nh1, nw1 = h1 + dh, w1 + dw
            nh2, nw2 = h2 + dh, w2 + dw
            if 0 <= nh1 < H and 0 <= nw1 < W:
                grid[nh1][nw1] = True
            if 0 <= nh2 < H and 0 <= nw2 < W:
                grid[nh2][nw2] = True
    for h in range(H):
        for w in range(W):
            if grid[h][w] and S[h][w] == ".":
                ret += 1
    return ret


H, W, D = map(int, input().split())
S = list(input() for _ in range(H))

ok = []

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            ok.append((h, w))

ans = 0
for p1, p2 in combinations(ok, 2):
    ans = max(ans, humid(p1[0], p1[1], p2[0], p2[1]))

print(ans)
