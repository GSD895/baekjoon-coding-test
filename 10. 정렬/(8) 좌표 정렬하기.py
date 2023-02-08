num = int(input())
lst = []

for i in range(0,num):
  a,b=map(int,input().split())
  lst.append([a,b])

lst=sorted(lst)
for i in lst:
  print(*i) #괄호 컴마 없이 출력하기