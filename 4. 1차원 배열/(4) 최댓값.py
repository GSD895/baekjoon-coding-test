lst = []
for i in range(0,9):
  x = int(input())
  lst.append(x)
print(max(lst))
print(lst.index(max(lst))+1)