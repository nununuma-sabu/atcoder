"""
N行N列のグリッド ※Nは偶数
グリッドの各マスは白黒で塗られている

i = 1,2,...,N/2の順に以下の操作
・i以上N+1-i以下の整数x,yについて (y, N+1-x)の色を(x, y)の色で置き換える


1: 1 <= x,y <= N
2: 2 <= x,y <= N - 1
3: 3 <= x,y <= N - 2
…
N/2: N/2 <= x,y <= N/2 + 1
つまり
1回目(1,1)~(N,N)を右に90度回転
2回目(2,2)~(N-1,N-1)を右に90度回転
3回目(3,3)~(N-2,N-2)を右に90度回転
…
N/2回目(N/2,N/2)~(N/2+1,N/2+1)を右に90度回転


4回周期っぽい
"""

N = int(input())
A = [list(input()) for _ in range(N)]
B = [[""] * N for _ in range(N)]

for h in range(N):
    for w in range(N):
        cnt = min(h + 1, N - h, w + 1, N - w)
        x = h
        y = w
        for k in range(cnt % 4):
            tmp_x = y
            tmp_y = N - 1 - x
            x = tmp_x
            y = tmp_y
        B[x][y] = A[h][w]

for b in B:
    print("".join(b))
