args = input().split(" ")
n = int(args[0])
y = int(args[1])/1000
#print(n,y)

for i in range(n+1):
    for j in range(n+1):
        ny = 9*i + 4*j
        if (ny == y-n and n-i-j >= 0):
            print(i,j,n-i-j)
            exit()
print("-1 -1 -1")
