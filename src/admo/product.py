a = input()
b,c = a.split(" ")
r = int(b)*int(c)
if r%2 == 0:
    print("Even")
else:
    print("Odd")
