a = int(input())
b = int(input())
c = int(input())
x = int(input())/50

ans = 0

for i in range(a+1):
    #print("a:%d", i)
    for j in range(b+1):
        for k in range(c+1):
            nx = 10*i + 2*j + k
            #print(nx,x)
            if (nx == x):
                ans = ans + 1

print(ans)

