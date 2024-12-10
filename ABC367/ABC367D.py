N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)

# 2周分カウントしたい
A += A

# Mで割ったあまりの個数をカウント
c = [0] * M
d = 0
ans = 0

for i in range(2 * N):
    if i >= N:
        c[(d - s) % M] -= 1
        ans += c[d % M]
    c[d % M] += 1
    d += A[i]
# print(c)
print(ans)
