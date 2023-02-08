import sys
num = int(sys.stdin.readline())
lst = []

for i in range(0,num):
  a,b=map(int,sys.stdin.readline().split())
  lst.append([a,b])
  
lst.sort(key = lambda x: x[0])
lst.sort(key = lambda x: x[1])
for i in lst:
  print(*i)  #괄호 컴마 없이 출력하기