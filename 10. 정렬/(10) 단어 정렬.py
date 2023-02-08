import sys

num=int(sys.stdin.readline())
lst = []
length = []
for i in range(0,num):
  word= sys.stdin.readline().strip()
  lst.append(word)
lst=list(set(lst))
lst.sort()
lst.sort(key = lambda x: len(x))

for i in lst:
  print(i)