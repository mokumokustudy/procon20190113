n = int(input())
ais = input().split(" ")
l = [int(s) for s in ais]

alice = 0
bob = 0
index = 0
for i in sorted(l):
    if len(l) % 2 == 0:
        if index % 2 == 0:
            bob = bob + i
        else:
            alice = alice + i
    else:
        if index % 2 == 0:
            alice = alice + i
        else:
            bob = bob + i
    index = index + 1
print(alice - bob)
