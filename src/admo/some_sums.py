i = input().split(" ")
n = i[0]
a = int(i[1])
b = int(i[2])

sum = 0
for i in range(int(n),0,-1):
    #print("i:%d\n",i)
    s = 0
    for d in range(len(str(i))):
        v = str(i)[d:d+1]
        s = s + int(v)
    if s >= a and s <= b:
        sum = sum + i
print(sum)
