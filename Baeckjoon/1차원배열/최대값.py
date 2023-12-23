#2562
import sys
input = sys.stdin.readline

# arr = list(map(int,input().split())) ->> 띄어쓰기 간격으로 값 입력받을 때

arr = []

for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1)