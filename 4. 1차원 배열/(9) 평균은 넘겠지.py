case=int(input())
for i in range(0,case):
  lst=list((input().split()))
  scores = []
  for i in lst:
    scores.append(int(i))
  avg=(sum(scores)-scores[0])/scores[0]
  count=0
  for i in range(1,len(scores)):
    if(scores[i]>avg):
      count = count +1
  ans=count/(len(scores)-1)
  print(f'{"{:.3f}".format(ans*100)}%')
 