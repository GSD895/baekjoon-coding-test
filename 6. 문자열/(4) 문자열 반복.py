num=int(input())
for i in range(0,num):
  count, word= (input().split())
  count = int(count)
  word = list(word)
  ans = []
  for i in word:
    for k in range(0,count):
      ans.append(i)

  print(''.join(ans))