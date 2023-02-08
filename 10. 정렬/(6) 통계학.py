import math
num=int(input())
lst = []
for i in range(0,num):
  a=int(input())
  lst.append(a)
lst=sorted(lst)
K=(len(lst)-1)//2
MAX=0
#산술평균
A= round(sum(lst)/len(lst))
#중앙값
B=lst[K]
#최빈값
C=[]
for i in lst:
  if(MAX<lst.count(i)):
    MAX = lst.count(i)
for i in lst:
  if(MAX==lst.count(i)):
    C.append(i)
C=list(sorted(set(C)))
if(len(C)>1):
  C = int(C[1])
else:
  C = int(C[0])
#범위
D=lst[-1]-lst[0]

print(A)
print(B)
print(C)
print(D)