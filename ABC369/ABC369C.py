N = int(input())
A = list(map(int, input().split()))

# 隣の差分を取る
D = [A[i + 1] - A[i] for i in range(N - 1)]

ans = N

# Dの中で同じ数字が何個続いてるかを数える
combo = 0

for i in range(N - 1):
    if i > 0 and D[i] == D[i - 1]:
        combo += 1
    else:
        combo = 1
    ans += combo
print(ans)
