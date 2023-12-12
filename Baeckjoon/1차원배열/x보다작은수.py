#10871번
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
num_list = list(map(int,input().split()))
if (num_list<b):
    print(num_list)