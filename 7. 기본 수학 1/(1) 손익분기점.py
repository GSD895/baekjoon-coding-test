import math
a,b,c = map(int, input().split())
if (c>b):
  k = math.floor(a/(c-b))+1
elif (c<b):
  k=-1
elif(a==0):
  k=0
else:
  k=-1
print(k)