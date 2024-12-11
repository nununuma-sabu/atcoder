N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    tmp = [x for x in enumerate(A) if x[1] == i]
    if abs(tmp[0][0] - tmp[1][0]) == 2:
        ans += 1

print(ans)
