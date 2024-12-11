"""
石移しゲーム
1-NまでのN個のマスがある
最初はM個のマスに石が入っている
マスX[i]にはA[i](1<=i<=M)個の石

以下の操作を好きなだけ行える(0回でも可)
・マスi(1<=i<=N-1)に石があるとき、石を1個マスiからマスi+1に移す

N個のマス全てにちょうど1個ずつ入っている状態にするための最小の操作回数
※不可能な場合は-1
"""

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# M個のマスに入っている石の合計がNでなければ絶対ダメ
if sum(A) != N:
    print(-1)
    exit()

num = 0

# Nマスに1個ずつ入っている場合の石の番号の総和
# 1 + 2 + ... + N = N*(N+1)//2
# A[i] * X[i]ずつ引いていく

ans = N * (N + 1) // 2

for x, a in sorted(zip(X, A), key=lambda x: x[0]):
    if num < x - 1:
        ans = -1
        break
    num += a
    ans -= x * a
print(ans)
