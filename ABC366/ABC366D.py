# 三次元累積和的なことをやる
N = int(input())
A = []
for _ in range(N):
    a = [list(map(int, input().split())) for _ in range(N)]
    A.append(a)

s = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            s[i + 1][j + 1][k + 1] = (
                s[i + 1][j + 1][k]
                + s[i + 1][j][k + 1]
                + s[i][j + 1][k + 1]
                - s[i + 1][j][k]
                - s[i][j + 1][k]
                - s[i][j][k + 1]
                + s[i][j][k]
                + A[i][j][k]
            )

Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    Lx -= 1
    Ly -= 1
    Lz -= 1
    print(
        s[Rx][Ry][Rz]
        - s[Lx][Ry][Rz]
        - s[Rx][Ly][Rz]
        - s[Rx][Ry][Lz]
        + s[Lx][Ly][Rz]
        + s[Lx][Ry][Lz]
        + s[Rx][Ly][Lz]
        - s[Lx][Ly][Lz]
    )
