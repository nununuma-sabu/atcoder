S = input()
N = len(S)
M = 128  # 英大文字のASCIIコード(65-90)まで収められるように大きめに

s = [[0] * (N + 1) for _ in range(M)]  # 文字の登場回数の累積和

for i in range(M):
    for j in range(N):
        s[i][j + 1] = s[i][j] + (ord(S[j]) == i)

ans = 0
for i in range(M):
    for j in range(N):
        ans += s[i][j] * (s[i][N] - s[i][j + 1])

print(ans)
