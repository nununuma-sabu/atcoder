N = int(input())

ans = 0
pre_l = -1
pre_r = -1

for _ in range(N):
    A, S = input().split()
    A = int(A)
    if S == "L":
        if pre_l == -1:
            pre_l = A
        else:
            ans += abs(A - pre_l)
            pre_l = A
    else:
        if pre_r == -1:
            pre_r = A
        else:
            ans += abs(A - pre_r)
            pre_r = A

print(ans)
