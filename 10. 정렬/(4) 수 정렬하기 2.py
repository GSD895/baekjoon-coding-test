def merge(lst, lst2):
  i=0
  j=0
  ans=[]
  for k in range(0,len(lst)+len(lst2)):
    if(lst[i]<lst2[j]):
      ans.append(lst[i])
      i = i+1
    else:
      ans.append(lst2[j])
      j = j+1
    if(i>=len(lst)):
      ans= ans+lst2[j:]
      return ans
      break
    if(j>=len(lst2)):
      ans = ans+lst[i:]
      return ans
      break

def mergeSort(array):
  if len(array) <= 1:
        return array
  mid = len(array) // 2
  left = array[:mid]
  right = array[mid:]
  left = mergeSort(left)
  right = mergeSort(right)
  return merge(left, right)

num=int(input())
lst = []
for i in range(0,num):
  a=int(input())
  lst.append(a)
lst=mergeSort(lst)

for i in range(0,num):
  print(lst[i])