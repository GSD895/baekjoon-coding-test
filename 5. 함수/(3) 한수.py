def hansu(num : int):
  lst = []
  for i in range(1,100):
    lst.append(i)
  for k in range(1,10):
    for i in range(-4,5): 
      if (10>k+i>0 and 10>k+(2*i)>=0):
        lst.append(k*100 + (k+i)*10 + (k+(2*i)))

  count = 0
  for i in lst:
    if(num-i>=0):
      count= count+1
    else:
      break
  print(count)

k=int(input())
hansu(k)