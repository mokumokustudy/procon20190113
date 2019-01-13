N = int(input())
A = list(map(int, input().split()))

count = 0

while True:
    _A = []
    for a in A:
        if (a % 2) == 0:
            _A.append(a / 2)
    if (N == len(_A)):
        count += 1
        A = _A
    else:
        break

print(count)