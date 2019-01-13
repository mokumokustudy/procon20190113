n = int(input())
l = []
for i in range(n):
    l.append(input())

l = sorted([int(s) for s in set(l)])
print(len(l))



