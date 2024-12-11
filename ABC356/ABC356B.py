# N：品数 M:栄養素の数
N, M = map(int, input().split())

# 目標
A = list(map(int, input().split()))

ret = [0] * M

for i in range(N):
    X = list(map(int, input().split()))
    for i in range(M):
        ret[i] += X[i]

if all([ret[i] >= A[i] for i in range(M)]):
    print("Yes")
else:
    print("No")
