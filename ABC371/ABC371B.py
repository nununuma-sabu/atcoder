N, M = map(int, input().split())
F = [0] * (N + 1)

for _ in range(M):
    a, b = input().split()
    a = int(a)
    if b == "M":
        if F[a] == 0:
            print("Yes")
        else:
            print("No")
        F[a] += 1
    else:
        print("No")
