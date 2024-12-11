# N個のおみやげ M人に配る
# おみやげには1個1円のお菓子がA[i]個入っている
# 人jにはB[i]個以上のお菓子が入った箱を渡す必要あり
# 最低何円で全員に配れるか

from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = SortedList(A)
ans = 0

for b in B:
    idx = S.bisect_left(b)
    if idx == len(S):
        ans = -1
        break
    ans += S[idx]
    S.pop(idx)

print(ans)
