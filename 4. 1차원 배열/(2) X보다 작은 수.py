N, X = map(int,input().split())
lst = list(map(int,input().split()))
ans = []
for i in lst:
  if (X>i):
    ans.append(i)

result_string = ' '.join(map(str, ans))
print(result_string)
