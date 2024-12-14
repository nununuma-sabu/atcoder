# 2×4の図形が1単位
# 面積を累積和で管理する
def f(y, x):
    S = [[0, 0, 0, 0, 0], [0, 2, 3, 3, 4], [0, 3, 6, 7, 8]]
    sub1 = (y // 2) * (x // 4) * S[2][4]
    sub2 = (y // 2) * S[2][x % 4]
    sub3 = (x // 4) * S[y % 2][4]
    sub4 = S[y % 2][x % 4]
    return sub1 + sub2 + sub3 + sub4


A, B, C, D = map(int, input().split())
A += 10**9
B += 10**9
C += 10**9
D += 10**9

ans = f(D, C) - f(D, A) - f(B, C) + f(B, A)
print(ans)
