"""
N人のお客
人iの美食度はA[i]

M個の寿司がレーンを流れる
j番目の寿司の美味しさはB[j]

それぞれの人は美味しさが自分の美食度以上の寿司が流れてきたら食べる
それ以外のときは何もしない
人iが食べた寿司は人j(j>i)の前には流れてこない
M個の寿司それぞれについて、その寿司を誰が食べるかあるいは誰も食べないか答える
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = 200010

# 美味しさiの寿司を誰が最初に食べるかリスト
id = [-1] * K

r = K

# 人i A[i]~美味しさ上限の寿司を食べる権利を得る
for i in range(N):
    while r > A[i]:
        r -= 1
        id[r] = i + 1

for i in range(M):
    print(id[B[i]])
