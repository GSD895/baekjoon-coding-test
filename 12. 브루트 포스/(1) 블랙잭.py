import sys

def blackjack (n, m, lst):
    ans = []
    n_ans = []
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                ans.append(lst[i]+lst[j]+lst[k])
    ans=set(ans)
    for i in ans:
        if(i<=m):
            n_ans.append(i)
    return max(n_ans)

n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
print(blackjack(n,m,lst))