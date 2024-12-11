"""
10**100個の植木鉢
最初は植物は1個も育てていない

Q個のクエリ
1:高さ0の植物を1個植える
2 T:T日待って全ての植物の高さがT増加
3 H:高さH以上の植物を全て収穫 収穫した植物の数を出力
"""

from collections import deque

Q = int(input())
q = deque()
d = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.append(d)
    elif query[0] == 2:
        d += query[1]
    else:
        c = 0
        # ex.15日目に植えて、30日目に高さ10以上が収穫されることを考える
        # 15日目:0 → 30日目:15 収穫対象
        # 30日目に高さが10以上となる→20日目以前に植えられている必要がある
        while q and q[0] <= d - query[1]:
            c += 1
            q.popleft()
        print(c)
