# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc081_a

import sys

def gets(input):
    return input.readline().strip()

def run(input):
    line = gets(input)
    n = 0
    for ch in line:
        if ch == '1':
            n += 1
    return n

def main():
    result = run(sys.stdin)
    print(result)

main()
