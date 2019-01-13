N, A, B = map(int, [input() for i in range(3)])

count = 0

for i in range(N + 1):
    _i = 0
    for j in list(str(i)):
        _i += int(j)
    if (_i >= A and _i <= B):
        count += i

print(count)