import sys

num=int(sys.stdin.readline())

def fibonacci (num):
    if num==1:
        return 0
    if num==2:
        return 1
    ans = fibonacci(num-1)+fibonacci(num-2)
    return ans

print(fibonacci(num+1))