a = input()
c = 0
for i in range(len(a)):
    v = a[i:i+1]
    if int(v) == 1:
        c = c + 1
print(c)
