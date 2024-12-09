N = int(input())
K = list(map(int, input().split()))

S = sum(K)
ans = 1 << 60

for i in range(1 << N):
    A = 0
    for j in range(N):
        if i & (1 << j):
            A += K[j]
    ans = min(ans, max(A, S - A))

print(ans)
