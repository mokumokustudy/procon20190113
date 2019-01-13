# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc087_b

import sys

def gets(input):
    return input.readline().strip()

def solve500(x, a, b, c):
    n = 0
    for i in range(0, a+1):
        if i * 500 > x:
            break
        n += solve100(x - i * 500, b, c)
    return n

def solve100(x, b, c):
    n = 0
    for i in range(0, b+1):
        if i * 100 > x:
            break
        n += solve50(x - i * 100, c)
    return n

def solve50(x, c):
    if x % 50 == 0 and x // 50 <= c:
        return 1
    else:
        return 0

def run(input):
    a = int(gets(input))
    b = int(gets(input))
    c = int(gets(input))
    x = int(gets(input))
    #
    return solve500(x, a, b, c)

def main():
    result = run(sys.stdin)
    print(result)

main()
