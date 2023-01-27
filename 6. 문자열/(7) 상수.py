A,B=list(input().split())
a= list(A)
b= list(B)
a.reverse()
b.reverse()
a=int(''.join(a))
b=int(''.join(b))

if (a>b):
  print(a)
else:
  print(b)