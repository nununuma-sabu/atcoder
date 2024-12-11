N, M = map(int, input().split())
H = list(map(int, input().split()))

nokori = M
ans = 0

for h in H:
    if nokori - h >= 0:
        nokori -= h
        ans += 1
    else:
        break

print(ans)
