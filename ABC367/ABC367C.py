N, K = map(int, input().split())
R = list(map(int, input().split()))


def solve(i, A):
    if i == N:
        if sum(A) % K == 0:
            print(" ".join(map(str, A)))
    else:
        for j in range(1, R[i] + 1):
            A.append(j)
            solve(i + 1, A)
            A.pop()


solve(0, [])
