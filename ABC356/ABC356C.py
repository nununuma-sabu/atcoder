# N:鍵の数 M:試行回数 K:正しい鍵をK本以上挿すと開く
N, M, K = map(int, input().split())

# C:挿し込む鍵の数 A:挿し込む鍵のリスト R:開いたかどうか
C, A, R = [], [], []

for _ in range(M):
    X = list(input().split())
    C.append(int(X[0]))
    A.append(list(map(int, X[1:-1])))
    R.append(X[-1])

ans = 0

for bits in range(1 << N):
    ok = True
    for i in range(M):
        cnt = 0
        for a in A[i]:
            cnt += (bits >> (a - 1)) & 1
        ok &= (cnt >= K) == (R[i] == "o")
    ans += ok
print(ans)
