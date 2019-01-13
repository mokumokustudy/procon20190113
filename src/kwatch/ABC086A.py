# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc086_a

import sys

def gets(input):
    return input.readline().strip()

def run(input):
    a, b = gets(input).split()
    x = int(a) * int(b)
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    result = run(sys.stdin)
    print(result)

main()
