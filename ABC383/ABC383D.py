"""
N以下の整数のうち、正の約数を9個持つものの個数
"""

from bisect import bisect_right


# エラトステネスのふるい
def era(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    res = []
    for i in range(2, N + 1):
        if is_prime[i]:
            res.append(i)
            for j in range(i * 2, N + 1, i):
                is_prime[j] = False
    return res


N = int(input())
# √Nまでの素数
p = era(int(N**0.5))

# 素数の2乗のリスト
p2 = [x**2 for x in p]

ans = 0
# まずは素数の8乗 これは約数が9個になる
for x in p:
    if x**8 <= N:
        ans += 1

# 次は相違なる素数p,qを使ってp**2 * q**2 のもののうちN以下のものの個数
for i in range(len(p)):
    pos = bisect_right(p2, N // p2[i], lo=i + 1)
    ans += pos - i - 1

print(ans)
