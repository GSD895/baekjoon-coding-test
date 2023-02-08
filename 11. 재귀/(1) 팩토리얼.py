import sys

num=int(sys.stdin.readline())

def factorial (num):
    if num<=1:
        return 1
    ans= factorial(num-1)* num
    return ans

print(factorial(num))