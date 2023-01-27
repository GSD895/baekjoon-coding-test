cost= int(input())
num= int(input())
lst = []
for i in range(0,num):
  x,y= list(map(int, input().split()))
  lst.append(x*y)
if(sum(lst)==cost):
  print('Yes')
else:
  print('No')
  
