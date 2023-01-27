lst = list(map(int, input().split()))

print((lst[0]+lst[1])%lst[2])
print(((lst[0]%lst[2])+(lst[1]%lst[2]))%lst[2])
print(lst[0]*lst[1]%lst[2])
print(((lst[0]%lst[2])*(lst[1]%lst[2]))%lst[2])
