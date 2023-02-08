import sys

lane = []
sort_lane = []
ans= []
num=int(sys.stdin.readline())
lane= list(map(int,sys.stdin.readline().split()))
# print(lane)
sort_lane= sorted(list(set(lane)))
# print(sort_lane)
dic = {sort_lane[i]:i for i in range (len(sort_lane))}

for i in lane:
  print(dic[i],end=' ')