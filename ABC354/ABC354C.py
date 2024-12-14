# 強さ:A[i] コスト:C[i]
# 同じ強さならコストが低い方が強い
N = int(input())

# x軸：A[i] y軸C[i]でプロット
# x軸の右から見ていく

pos = []
for i in range(N):
    A, C = map(int, input().split())
    pos.append((A, C, i + 1))

pos.sort()
ans = []
min_c = 1 << 60

for A, C, i in pos[::-1]:
    if C < min_c:
        min_c = C
        ans.append(i)

ans.sort()
print(len(ans))
print(*ans)
