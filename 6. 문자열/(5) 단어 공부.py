import sys
string=list(sys.stdin.readline().lower())
lst=set(string)
lst2 = []
for i in lst:
  lst2.append(string.count(i))
if (lst2.count(max(lst2))>1):
  print('?')
else:
  print(max(string, key=string.count).upper())