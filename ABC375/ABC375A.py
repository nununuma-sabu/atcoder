N = int(input())
S = input()

ans = 0

for i in range(2, N):
    if S[i - 2] == S[i] == "#" and S[i - 1] == ".":
        ans += 1

print(ans)
