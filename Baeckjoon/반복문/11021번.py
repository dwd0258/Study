#11021번
#A+B-7

import sys
input = sys.stdin.readline

n= int(input())

for i in range(1,n+1):
    a,b = map(int,input().split())
    print("Case #%d: %d"%i,a+b)
    
    
    '''
    print("Case #"+str(i)+':',a+b)
    print("Case #%s: %s"%(i+1, ans ))
    '''