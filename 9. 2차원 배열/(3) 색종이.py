num=int(input())
paper = [[0 for x in range(100)] for y in range(100)]
count = 0

for i in range(0,num):
   a,b=map(int, input().split())
   for x in range(a,a+10):
      for y in range(b,b+10):
         paper[x][y]=1

for x in range(0,100):
   for y in range(0,100):
      if(paper[x][y]==1):
         count = count+1

print(count)