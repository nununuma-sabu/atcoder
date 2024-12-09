"""
以下の条件を満たす数列Aを辞書順に全て出力
・1<=A[i]
・2<=i<=Nに対して A[i-1] + 10 <= A[i]
・A[N] <= M
"""

N, M = map(int, input().split())

ans = []


# 再帰で解く
def solve(a, x):
    if len(a) == N:
        ans.append(a[:])
    else:
        # 最大値 - 10 * (数列Aの長さ - 1 - 現在の数列aの長さ + 1)
        for i in range(x, M - 10 * (N - 1 - len(a)) + 1):
            a.append(i)
            solve(a, i + 10)
            a.pop()


solve([], 1)
print(len(ans))
for a in ans:
    print(*a)
