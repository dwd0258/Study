#10950번
#A+B-3

import sys
input = sys.stdin.readline

n= int(input())

for i in range (1,n+1):
    a,b = map(int,input().split())
    print(a+b)