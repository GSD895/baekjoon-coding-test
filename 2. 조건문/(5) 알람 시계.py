x, y = map(int, input().split())

if(y>=45):
  print(x, y-45)
else:
  if(x>0):
    print(x-1, y+15)
  else:
    print(23, y+15)
