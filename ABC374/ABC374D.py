"""
N本の線分を印字したい
i本目は座標(A[i],B[i]) と 座標(C[i],D[i])を結ぶ

印字中→毎秒T 印字していない→毎秒Sで移動できる
全ての線分を印字完了するまでの最短時間
"""

from itertools import permutations

N, S, T = map(int, input().split())
ans = 1 << 60

# 線分の長さの合計は不変→あらかじめ保存しておく(速度Tで何秒かかるか)
base = 0

A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    base += (((a - c) ** 2 + (b - d) ** 2) ** 0.5) / T

order = [i for i in range(N)]

# 印刷する線分の順序→permutations
for p in permutations(order):
    # 線分のどちらの端から印字するか→ビット全探査
    for bit in range(1 << N):
        dis = base
        # 始点と終点を保存する配列dis
        sx, sy, tx, ty = [], [], [], []
        for i in range(N):
            idx = p[i]
            if bit & (1 << i):
                sx.append(A[idx])
                sy.append(B[idx])
                tx.append(C[idx])
                ty.append(D[idx])
            else:
                sx.append(C[idx])
                sy.append(D[idx])
                tx.append(A[idx])
                ty.append(B[idx])
        # 原点から1本目の線分の始点(速度Sで何秒かかるか)
        dis += ((sx[0] ** 2 + sy[0] ** 2) ** 0.5) / S
        for i in range(N - 1):
            dx = abs(sx[i + 1] - tx[i])
            dy = abs(sy[i + 1] - ty[i])
            dis += ((dx**2 + dy**2) ** 0.5) / S
        ans = min(ans, dis)

print(ans)
