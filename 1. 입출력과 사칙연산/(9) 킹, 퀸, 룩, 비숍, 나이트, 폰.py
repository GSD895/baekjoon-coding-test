lst = list(map(int, input().split()))
chess = [1,1,2,2,2,8]
ans = []
for i in range(0,6):
  ans.append(chess[i]-lst[i])
ans= " ".join(str(x) for x in ans)
print(ans)

map