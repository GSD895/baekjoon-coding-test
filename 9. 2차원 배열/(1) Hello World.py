rows,cols = map(int, input().split())
lst1 = []
lst2 = []
ans = [[0]*cols for i in range(rows)]
for i in range(0,rows):
  lst=list(input().split())
  lst1.append(lst)

for i in range(0,rows):
  lst=list(input().split())
  lst2.append(lst)

for i in range(0,rows):
  for k in range(0, cols):
    ans[i][k] = int(lst1[i][k]) + int(lst2[i][k]) 
for i in range(0, rows):
  print(*ans[i])