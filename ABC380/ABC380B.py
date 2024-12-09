S = list(input().split("|"))

ans = []

for s in S:
    if s == "":
        continue
    ans.append(len(s))

print(*ans)
