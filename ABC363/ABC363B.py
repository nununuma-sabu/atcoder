# N人の人がいる 髪の長さはL[i] 全員1日あたり髪の長さが1増える
# 髪の長さがT以上の人が初めてP人以上になるのは何日後
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

ans = 0
while True:
    if len(list(filter(lambda x: x + ans >= T, L))) >= P:
        print(ans)
        break
    ans += 1
