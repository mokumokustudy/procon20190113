# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/abc088_b

import sys

def run(nums):
    nums = sorted(nums, reverse=True)
    alice_point = sum(nums[0::2])
    bob_point   = sum(nums[1::2])
    return alice_point - bob_point

def main():
    def gets(input=sys.stdin):
        return input.readline().strip()
    N = int(gets())
    arr = [ int(x) for x in gets().split() ]
    assert len(arr) == N
    result = run(arr)
    print(result)

main()
