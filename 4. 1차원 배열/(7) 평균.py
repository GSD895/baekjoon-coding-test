num = int(input())
scores = []
new_scores = []
scores=list(map(int, input().split()))

for i in range(0,num):
  new_scores.append(scores[i]/max(scores)*100)
print(sum(new_scores)/num)