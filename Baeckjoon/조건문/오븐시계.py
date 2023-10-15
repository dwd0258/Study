#2525번

import sys
input = sys.stdin.readline

A,B = map(int,input().split())
C= int(input())

if (B+C) >= 60:
    C1= (B+C)//60
    C2= (B+C)%60
    
    if (A+C1) > 23:
        print((A+C1)-24,C2)
    else :
        print((A+C1),C2)
        
else : #(B+C) < 60
    print(A,B+C)
