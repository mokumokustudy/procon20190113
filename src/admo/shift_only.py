a = input()
b = input()
#print(a)
l = b.split(" ")
c = 0

while(1):
    list = [1 for item in l if int(item) % 2 == 0]
    if len(list) == int(a):
        c = c + 1
        l = [int(item)/2 for item in l]
        #print(l)
    else:
        break
print(c)
