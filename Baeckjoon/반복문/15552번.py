#15552번
#빠른 A+B

import sys
input = sys.stdin.readline

n= int(input())

for i in range(1,n+1):
    a,b = map(int,input().split())
    print(a+b)