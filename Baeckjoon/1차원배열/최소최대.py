#10818번
import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int,input().split()))

#1
# mn = min(a_list)
# mx = max(a_list)
# print(mn,mx) 

#2
#print(min(a_list),max(a_list))

#3
# min = a_list[0]
# max = a_list[0]
# for i in range(n):
#     if a_list[i] > max :
#         max = a_list[i]
#     elif a_list[i] < min:
#         min = a_list[i]
# print(min,max)

a_list.sort()
print(a_list[0],a_list[n-1])