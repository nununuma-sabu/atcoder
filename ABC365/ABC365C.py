N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) <= M:
    print("infinite")
    exit()


# 交通費補助の上限がM以下になるか
def solve(x):
    s = 0
    for a in A:
        s += min(x, a)
    return s <= M


ok = 0
ng = max(A)

while ok + 1 < ng:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)
