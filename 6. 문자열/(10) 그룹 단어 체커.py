num=int (input())
count=0

for i in range(0,num):
  word = list(input())
  alpha = []
  pandan=1

  for i in range(0,len(word)):
    if (word[i] in alpha):
      if(word[i-1]==word[i]):
        pass
      else:
        pandan = -1
    else:
      alpha.append(word[i])
  if (pandan==1):
    count = count+1
  elif(pandan ==-1):
    pass

print(count)