N = int(input())
T = 0

player = []

for _ in range(N):
    s, c = input().split()
    T += int(c)
    player.append(s)

player.sort()

ret = dict()

for i, s in enumerate(player):
    ret[i] = s

print(ret[T % N])
