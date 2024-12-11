def cost(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


N = int(input())

X, Y = [], []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = cost(0, 0, X[0], Y[0])

for i in range(N - 1):
    x1 = X[i]
    y1 = Y[i]
    x2 = X[i + 1]
    y2 = Y[i + 1]
    ans += cost(x1, y1, x2, y2)

ans += cost(X[-1], Y[-1], 0, 0)

print(ans)
