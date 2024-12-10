# B[i] = A[X[i]]となるBを新たなAとする
# K回繰り返したらどうなるか
# ダブリング
# 1->2->4->16->... と作る
# 2の累乗以外の数は2の累乗の和で表せる
N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))


def solve(x, p):
    if p == 0:
        return [i for i in range(N)]
    elif p % 2 == 0:
        y = solve(x, p // 2)
        return [y[v] for v in y]
    else:
        y = solve(x, p - 1)
        return [y[v] for v in x]


x = solve([v - 1 for v in X], K)
print(" ".join(map(str, [A[v] for v in x])))
