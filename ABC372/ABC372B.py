M = int(input())
ans = []

while M > 0:
    A = 10
    while 3**A > M:
        A -= 1
    ans.append(A)
    M -= 3**A

print(len(ans))
print(*ans)
