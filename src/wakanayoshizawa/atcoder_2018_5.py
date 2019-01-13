import math

A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

if (A > math.floor(X / 500)):
    _X = X - (math.floor(X / 500) * 500)
else:
    _X = X - (A * 500)

if (B > math.floor(_X / 100)):
    __X = _X - (math.floor(_X / 100) * 100)
else:
    __X = _X - (B * 100)

if (C > math.floor(__X / 50)):
    ___X = __X - (math.floor(__X / 50) * 50)
else:
    ___X = __X - (C * 50)

if (___X == 0):
    count += 1
    if (A > math.floor(X / 500)):
        A = math.floor(X / 500)
    for a in range(1, A + 1):
        if (B >= a * 5):
            count += 1
        if (B >= a * 4 and C >= a * 2):
            count += 1
        if (B >= a * 3 and C >= a * 4):
            count += 1
        if (B >= a * 2 and C >= a * 6):
            count += 1
        if (B >= a * 1 and C >= a * 8):
            count += 1
    if (B > math.floor(X / 100)):
        B = math.floor(X / 100)
    for b in range(1, B + 1):
        if (C >= b * 2):
            count += 1
    if (C > math.floor(X / 50)):
        count += 1

print(count)