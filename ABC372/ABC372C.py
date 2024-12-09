# 長さNの文字列S
# SのX[i]番目の文字がC[i]になる
# その後、Sに"ABC"が何個含まれるか数える

N, Q = map(int, input().split())
# 番兵を仕込んで文字列をリスト化
S = list(".." + input() + "..")
cnt = 0
for i in range(N + 2):
    if S[i : i + 3] == ["A", "B", "C"]:
        cnt += 1

# 文字が変わった箇所の前後2つずつを見ればよい
for _ in range(Q):
    X, C = input().split()
    # インデックス計算分1を引いて、番兵分2を足す
    X = int(X) - 1 + 2
    for i in range(X - 2, X + 1):
        if S[i : i + 3] == ["A", "B", "C"]:
            cnt -= 1
    S[X] = C
    for i in range(X - 2, X + 1):
        if S[i : i + 3] == ["A", "B", "C"]:
            cnt += 1
    print(cnt)
