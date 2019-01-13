# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc083_b

import sys

def gets(input):
    return input.readline().strip()

def run(input):
    n, a, b = gets(input).split()
    N, A, B = int(n), int(a), int(b)
    #
    total = 0
    for i in range(1, N+1):
        x = sum( int(ch) for ch in str(i) )
        if A <= x <= B:
            total += i
    #
    return total

def main():
    result = run(sys.stdin)
    print(result)

main()
