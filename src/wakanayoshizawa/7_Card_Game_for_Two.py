N = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()

alice = 0
bob = 0

for i in range(1, len(a) + 1) :
    if (i % 2 == 0):
        bob += a[i - 1]
    else:
        alice += a[i - 1]
        
print(alice - bob)