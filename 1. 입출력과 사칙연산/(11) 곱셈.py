x=int(input())
y=int(input())

lsty= [y//100,int((y%100-y%10)/10),y%10]
print(x*lsty[2])
print(x*lsty[1])
print(x*lsty[0])
print(x*y)