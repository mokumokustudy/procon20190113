# -*- coding: utf-8 -*-

## https://atcoder.jp/contests/abs/tasks/practice_1

import sys

def gets(input):
    return input.readline().strip()

def run(input):
    a = gets(input)
    b, c = gets(input).split()
    s = gets(input)
    x = int(a) + int(b) + int(c)
    print("%s %s" % (x, s))

run(sys.stdin)

"""
kwatch@gmail.com
kaguya30859rasetai

"""
