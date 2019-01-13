N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n - i - j)
            exit()

print('-1 -1 -1')