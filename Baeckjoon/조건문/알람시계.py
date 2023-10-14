#2884번

import sys
input = sys.stdin.readline

H,M = map(int,input().split())

if M > 45: 
    print( H, M-45)
else :
     