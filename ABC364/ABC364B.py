H, W = map(int, input().split())
Sh, Sw = map(int, input().split())
Sh -= 1
Sw -= 1

C = [list(input()) for _ in range(H)]
X = input()
pos_h = Sh
pos_w = Sw

for x in X:
    if x == "L" and pos_w > 0 and C[pos_h][pos_w - 1] != "#":
        pos_w -= 1
    elif x == "R" and pos_w < W - 1 and C[pos_h][pos_w + 1] != "#":
        pos_w += 1
    elif x == "U" and pos_h > 0 and C[pos_h - 1][pos_w] != "#":
        pos_h -= 1
    elif x == "D" and pos_h < H - 1 and C[pos_h + 1][pos_w] != "#":
        pos_h += 1

print(pos_h + 1, pos_w + 1)
