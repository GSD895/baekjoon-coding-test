import sys

def sum (lst):
    sum = 0
    for i in lst:
        sum = sum+int(i)
    return sum

def bunhaehap (n) :
    lst=str(n)
    l = len(lst)
    check = 0
    min = 0
    if(n-9*l>0):
        min = n-9*l
    for i in range(min,n):
        if(i + sum(str(i))==n):
            check = 1
            return i
    if(check!=1):
        return 0

num=int(sys.stdin.readline())
print(bunhaehap(num))