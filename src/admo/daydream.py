s = input()
src = ['dreamer', 'eraser', 'dream', 'erase']

def hoge(s):
    #print("hoge",s,len(s))
    if len(s) == 0:
        return "YES"
    for w in src:
        pos = s.find(w)
        #print(pos)
        if (pos==0):
            ret = hoge(s[len(w):])
            if (ret == "YES"):
                return "YES"
    return "NO"
print(hoge(s))
