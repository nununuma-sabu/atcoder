N = int(input())
eve = []

for _ in range(N):
    l, r = map(int, input().split())
    eve.append((l, 0))
    eve.append((r, 1))

eve.sort()

ans = 0
cnt = 0

for _, t in eve:
    if t == 0:
        ans += cnt
    else:
        cnt += 1
# print(eve)
print(N * (N - 1) // 2 - ans)
