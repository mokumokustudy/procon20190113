# -*- coding: utf-8 -*-
 
N = int(input())
A = list(map(int, input().split()))
 
def reFunc(in_val, cnt):
  if in_val % 2 == 0:
    return reFunc(in_val // 2, (cnt + 1))
  else:
    return cnt
    
 
countAry = []
for i in range(N):
  countAry.append(reFunc(A[i], 0))
 
countAry.sort()
print(countAry[0])  