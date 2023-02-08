nums = []
for i in range(0,5):
  a=int(input())
  nums.append(a)

nums = sorted(nums)
sum=sum(nums)
avg = sum/5
mid = nums[2]

print(int(avg))
print(mid)