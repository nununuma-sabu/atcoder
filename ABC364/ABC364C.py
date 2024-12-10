# N個の料理
# 甘さA[i] しょっぱさB[i]
# 好きな順に食べて甘さ合計がX or しょっぱさ合計がYを超えたら終了
# 最低でも何個の料理を食べるか
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

sum1 = 0
sum2 = 0
ans1 = 0
ans2 = 0

for a in A:
    if sum1 > X:
        break
    sum1 += a
    ans1 += 1

for b in B:
    if sum2 > Y:
        break
    sum2 += b
    ans2 += 1

print(min(ans1, ans2))
