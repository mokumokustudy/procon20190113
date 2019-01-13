# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc081_b

import sys

def gets(input):
    return input.readline().strip()

def run(input):
    n = int(gets(input))
    arr = [ int(x) for x in gets(input).split() ]
    assert len(arr) == n
    #
    def div2(arr):
        arr2 = []; add = arr2.append
        for x in arr:
            if x % 2 == 0:
                add(x // 2)
            else:
                return None
        return arr2
    #
    count = 0
    while arr is not None:
        arr = div2(arr)
        count += 1
    return count - 1

def main():
    result = run(sys.stdin)
    print(result)

main()
