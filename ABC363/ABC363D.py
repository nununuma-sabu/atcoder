# 回分数
# 1桁 1,2,3,..,9 の9個
# 2桁 11,22,33,...,99 の9個
# 3桁 101,111,121,...,999 の90個
# 4桁 1001,1111,1221,...,9999 の90個
# 5桁 10001,10101,10201,...,99999 の900個
# ...

# 桁数をdとして、x=(d+1)//2とすると、
# ・d桁の回文数は9*10**(x-1)個
# ・k番目に小さいd桁の回文数の上位x桁を取り出してできる整数は
#   10**(x-1)+k-1


def ten(x):
    if x == 0:
        return 1
    else:
        return 10 * ten(x - 1)


N = int(input())

if N == 1:
    print(0)
    exit()

N -= 1
d = 1
while True:
    x = (d + 1) // 2
    if N <= 9 * ten(x - 1):
        S = list(str(ten(x - 1) + N - 1))
        # Sの長さをdに変更 大きくなった分はスペース埋め
        for _ in range(d - len(S)):
            S.append(" ")
        for i in range(x, d):
            S[i] = S[d - i - 1]
        print("".join(S))
        exit()
    else:
        N -= 9 * ten(x - 1)
        d += 1
