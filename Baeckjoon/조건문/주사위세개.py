#2480번

import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())
list = [A,B,C]

if A==B==C:
    print(10000+(A*1000))
elif A==B!=C:
    print(1000+(A*100))
elif A!=B==C:
    print(1000+(C*100))
elif A==C!=B:
    print(1000+(A*100))
elif A!=C!=B:
    print(max(list)*100)
    
'''
A,B,C = map(int,input().split())

if A==B==C:
    print(10000+(A*1000))
elif A==B!=C:
    print(1000+(A*100))
elif A!=B==C:
    print(1000+(C*100))
elif A==C!=B:
    print(1000+(A*100))
elif A!=C!=B:
    print(max(A,B,C)*100)
    
'''