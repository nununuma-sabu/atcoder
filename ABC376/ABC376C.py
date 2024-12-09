def makeC(x):
    C = sorted(B + [x])
    return C


def check(X, Y):
    for i in range(N):
        if X[i] > Y[i]:
            return False
    return True


N = int(input())
A = list(map(int, input().split()))
A.sort()

B = list(map(int, input().split()))

INF = 1 << 60
low = 0
high = INF

while low + 1 < high:
    mid = (low + high) // 2
    C = makeC(mid)
    if check(A, C):
        high = mid
    else:
        low = mid

if high < INF:
    print(high)
else:
    print(-1)
