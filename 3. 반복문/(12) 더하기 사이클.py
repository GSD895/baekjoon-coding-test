x= int(input())
count = 0
Turn = True
ten = x//10   
one = x%10
ten_0 = ten
one_0 = one
x=one*10+((ten+one)%10)

while Turn:
  ten = x//10
  one = x%10
  x=one*10+((ten+one)%10)
  count = count+1
  if(ten_0==ten and one_0==one):
    Turn=False

print(count)
