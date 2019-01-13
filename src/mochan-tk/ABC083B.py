# -*- coding: utf-8 -*-
N, A, B = map(int, input().split())

def specialFunc(in_val):
  lst = []
  j = in_val
  while j > 0:
    lst.append(j % 10)
    j //= 10

  if A <= sum(lst) <= B:
    return in_val 
  else:
    return 1

sumVal = 0
for i in range(N):
  sumVal = sumVal + specialFunc(i)

print(sumVal)