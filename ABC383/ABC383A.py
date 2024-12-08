N = int(input())
T, V = [], []

for _ in range(N):
    t, v = map(int, input().split())
    T.append(t)
    V.append(v)

ans = V[0]

for i in range(1, N):
    ans = max(0, ans - (T[i] - T[i - 1]))
    ans += V[i]

print(ans)
