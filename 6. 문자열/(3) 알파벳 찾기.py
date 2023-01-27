word=list(input())
ans = []
for i in range(97,123):
  if (chr(i)in word):
    ans.append(str(word.index(chr(i))))
  else:
    ans.append('-1')
ans=' '.join(ans)
print(ans)