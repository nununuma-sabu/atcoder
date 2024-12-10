X = list(input())

while X[-1] == "0":
    X.pop()

if X[-1] == ".":
    X.pop()

print("".join(X))
