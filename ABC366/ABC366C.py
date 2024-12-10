ball = [0] * (10**6 + 1)
cnt = 0

Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    typ = query[0]
    if typ == 1:
        x = query[1]
        if ball[x] == 0:
            cnt += 1
        ball[x] += 1
    elif typ == 2:
        x = query[1]
        ball[x] -= 1
        if ball[x] == 0:
            cnt -= 1
    else:
        print(cnt)
