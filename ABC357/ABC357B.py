S = input()
up, low = 0, 0
for s in S:
    if s.islower():
        low += 1
    else:
        up += 1

if low > up:
    print(S.lower())
else:
    print(S.upper())
