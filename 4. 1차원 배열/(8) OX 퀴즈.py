def panstar(lst : list) :
  count = 0
  score= 0
  for i in lst:
    if(i=='O'):
      count=count+1
      score=score+count

    else:
      count=0
  print(score)

num= int(input())
for i in range(0,num):
  ox= list(input())
  panstar(ox)
  ox= []