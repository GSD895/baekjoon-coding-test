nums = []
k=int(input())

for i in range(0,k):
  j=int(input())
  nums.append(j)

nums=sorted(nums)

for i in range(0,k):
  print(nums[i])