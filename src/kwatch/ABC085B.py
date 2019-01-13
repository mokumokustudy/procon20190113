# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc085_b

import sys

def run(nums):
    return len(set(nums))

def main():
    def gets(input=sys.stdin):
        return input.readline().strip()
    N = int(gets())
    arr = []; add = arr.append
    for _ in range(N):
        add(int(gets()))
    assert len(arr) == N
    #
    result = run(arr)
    print(result)

main()
