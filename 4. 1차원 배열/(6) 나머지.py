lst=[]
for i in range(0,10):
  x= int(input())
  lst.append(x%42)
  lst=list(set(lst))
  
print(len(lst))