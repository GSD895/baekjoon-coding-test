import sys
num= int(sys.stdin.readline())
for i in range(0,num):
  x,y= list(map(int, sys.stdin.readline().split()))
  print(x+y)
