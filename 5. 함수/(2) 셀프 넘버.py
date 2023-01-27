def noneselfnum():
  lst = []
  for i in range(1,10001):
    if (0<i<10):
      lst.append(i+i)
    if (10<=i<100):
      lst.append(i+i//10+i%10)
    if (100<=i<1000):
      lst.append(i+i//100+(i//10)%10+i%10)
    if (1000<=i<10000):
      lst.append(i+i//1000+(i//100)%10+(i//10)%10+i%10)
    lst = list(set(lst))
  return lst
  
def selfnumber ():
  lst = []
  noselfnum = []
  for i in range(1,10001):
    lst.append(i)
  noselfnum = noneselfnum()
  lst=sorted(list(set(lst).difference(noselfnum)))
  for i in lst:
    print(i)
selfnumber()

