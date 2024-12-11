S, T = input().split()

for w in range(1, len(S)):
    for c in range(w):
        tmp = []
        for i in range(c, len(S), w):
            tmp.append(S[i])
        if "".join(tmp) == T:
            print("Yes")
            exit()
print("No")
