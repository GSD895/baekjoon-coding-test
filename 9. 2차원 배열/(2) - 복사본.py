ans = []
for i in range(0,9):
  lst=list(map(int,input().split()))
  ans.append(lst)
print(max(map(max,ans)))

break_flag = False
for i in range(0, 9):
    for j in range(0, 9):
        if ans[i][j] == max(map(max, ans)):
            print(i+1, j+1)
            break_flag = True
            break
    if break_flag:
        break
