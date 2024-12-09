N, C = map(int, input().split())
T = list(map(int, input().split()))

ans = 1
pre = T[0]

for i in range(1, N):
    if T[i] - pre >= C:
        ans += 1
        pre = T[i]

print(ans)
