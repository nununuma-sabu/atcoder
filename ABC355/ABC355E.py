# Nおよび2**N未満の整数L.R
# 数列 A=(A[0],A[1],...,A[2**N-1]) をジャッジ側は持っている
# (0<=A[i]<=99)
# やりたいこと→A[L]+A[L+1]+...+A[R]を100で割った余りを求める
# こちらは質問ができる
# 2**i * (j+1) <= 2**Nを満たすように非負整数i,jを選んで
# l=2**i * j, r=2**i * (j+1)-1として
# A[l]+A[l+1]+...+A[r]を100で割った余りを聞ける
from collections import deque

N, L, R = map(int, input().split())
R += 1
MOD = 100

d = [-1] * ((1 << N) + 1)
pre = [(-1, -1)] * ((1 << N) + 1)
Q = deque()
d[L] = 0
Q.append(L)

while Q:
    x = Q.popleft()
    for i in range(N + 1):
        if x % (1 << i) == 0:
            for y in [x - (1 << i), x + (1 << i)]:
                if 0 <= y <= (1 << N) and d[y] == -1:
                    d[y] = d[x] + 1
                    pre[y] = i, x
                    Q.append(y)

ans = 0
x = R

while x != L:
    i, y = pre[x]
    print("?", i, min(x, y) >> i)
    T = int(input())
    if y < x:
        ans += T
    else:
        ans -= T
    x = y

print("!", ans % MOD)
