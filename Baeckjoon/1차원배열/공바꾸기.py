#10813번

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())  # n= 바구니 m= 공바꿀횟수
# arr = [i + 1 for i in range(n)] 

# for i in range(m):
#     a, b = map(int, input().split())
    
#     k = arr[a - 1]
#     arr[a - 1] = arr[b - 1]
#     arr[b - 1] = k
    
# print(*arr)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n= 바구니 m= 공바꿀횟수
arr = [i + 1 for i in range(n)] 

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    
    arr[a], arr[b] = arr[b], arr[a]
    
print(*arr)
