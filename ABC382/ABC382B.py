N, D = map(int, input().split())
S = input()

S = S[::-1]

S = S.replace("@", ".", D)
print(S[::-1])
