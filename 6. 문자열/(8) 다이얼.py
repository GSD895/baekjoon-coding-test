lst=[['1'],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z'],['0']]

phonenum=list(input())
time = 0
for k in phonenum:
  for i in range(0,10):
    if(k in lst[i]):
      time = time+i+2

print(time)