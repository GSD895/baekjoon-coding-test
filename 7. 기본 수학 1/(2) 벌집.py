import math
import sys
def way (i : int):
  return math.floor(math.sqrt((i-2)/3+1/4)+3/2)

i=int(sys.stdin.readline())
if (i == 1):
  print(1)
elif (1<i<8):
  print(2)
else:
  print(way(i))

# n = int(input())
# x = 1
# if n == 1:
#   print(1)
# else:
#   for i in range(1,n):
#     if x < n <= x + 6*i:
#         print(i+1)
#         break
#     x = x + 6*i