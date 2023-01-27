num= int(input())

for i in range(1,num+1):
  x,y =map(int, input().split())
  print(f'Case #{i}: {x} + {y} = {x+y}')