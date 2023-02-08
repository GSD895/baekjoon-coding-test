import sys

member = []
num=int(sys.stdin.readline())

for i in range(0,num):
    a,b = sys.stdin.readline().split()
    member.append([int(a),b])
    
member.sort(key= lambda x:x[0])

for i in member:
    print(*i)