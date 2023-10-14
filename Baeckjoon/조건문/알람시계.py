#2884번

import sys
input = sys.stdin.readline

H,M = map(int,input().split())

'''
1. (0 <= H <= 24) and ( M >= 45) 
print(H, M-45) 

2. (0 < H <= 24) and (M < 45)
print(H-1,(60+M)-45)

3. H == 0 and ( M >= 45)  >> 1번 때문에 없어도됨
print(H, M-45)

4. H == 0 and (M <45)
print(23,(60+M)-45)
'''

if (0 <= H <= 24) and ( M >= 45) : 
    print(H, M-45) 
elif (0 < H <= 24) and (M < 45):
    print(H-1,(60+M)-45)
elif H == 0 and (M <45):
    print(23,(60+M)-45)