A, B = map(int, input().split())
S = set([1, 2, 3])

S.discard(A)
S.discard(B)

if len(S) == 1:
    print(*S)
else:
    print(-1)
