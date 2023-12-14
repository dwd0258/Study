#10871번
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
num_list = list(map(int,input().split()))

for i in range(0,a): #(a)도 됨 0~ (a-1) 까지 (10)이면 0~9까지 10개
    if num_list[i] < b:
        print(num_list[i], end=" ")