import sys
cou=0
def recursion(s, l, r):
    global cou
    cou = cou+1
    if(l >= r): 
        return 1
    elif (s[l] != s[r]):
        return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

num=int(sys.stdin.readline())

for i in range(0,num):
    s=sys.stdin.readline().strip()
    print(f"{isPalindrome(s)} {cou}")
    cou = 0  