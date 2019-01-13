# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc085_c

import sys

def run(N, Y):
    for a, b, c in solve10000(N, Y):
        return a, b, c
    return -1, -1, -1

def solve10000(n, y):
    #for a in range(0, n+1):
    for a in range(n, -1, -1):
        if a * 10000 > y:
            continue
        for b, c in solve5000(n - a, y - a * 10000):
            yield a, b, c

def solve5000(n, y):
    #for b in range(0, n+1):
    for b in range(n, -1, -1):
        if b * 5000 > y:
            continue
        for c in solve1000(n - b, y - b * 5000):
            yield b, c

def solve1000(n, y):
    if y % 1000 == 0 and y // 1000 == n:
        yield n

def main():
    def gets(input=sys.stdin):
        return input.readline().strip()
    n, y = gets().split()
    N, Y = int(n), int(y)
    #
    a, b, c = run(N, Y)
    print("%s %s %s" % (a, b, c))

main()
