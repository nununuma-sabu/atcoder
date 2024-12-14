# N枚のカード
# 表にはA[i] 裏にはB[i]
# 表同士で同じ数 or 裏同士で同じ数 →その2枚を除く
# 除けなくなったら負け

# 2**18通りを全部試す
# 2**18 = 262144
N = int(input())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

DP = [False] * (2**N)

for mask in range(2**N):
    for i in range(N):
        for j in range(i + 1, N):
            if (
                (mask & (1 << i))
                and (mask & (1 << j))
                and (A[i] == A[j] or B[i] == B[j])
            ):
                DP[mask] |= not DP[mask ^ (1 << i) ^ (1 << j)]

if DP[2**N - 1]:
    print("Takahashi")
else:
    print("Aoki")
