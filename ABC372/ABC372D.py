# ビルがN棟ある
# ビルiから何個ビルが見えるかそれぞれのiで求める
# ビルiからビルjが見える条件→ビルiとビルjの間にビルjより高いビルがない
N = int(input())
H = list(map(int, input().split()))
S = []
ans = []

# 逆順で見ていくことにする
for h in H[::-1]:
    ans.append(len(S))
    while S and S[-1] < h:
        S.pop()
    S.append(h)

print(*ans[::-1])
