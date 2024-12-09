S = input()
T = input()
N = min(len(S), len(T))

if S == T:
    print(0)
    exit()
elif S[:N] == T[:N]:
    print(N + 1)
else:
    for i in range(N):
        if S[i] != T[i]:
            print(i + 1)
            break
