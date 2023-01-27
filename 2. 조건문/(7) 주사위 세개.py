F,S,T = map(int, input().split())
money = 0
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
if(F==S==T):
  money = 10000+F*1000
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
elif(F==S or S==T):
  money = 1000+S*100
elif(F==T):
  money = 1000+F*100
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
else:
  money = max(F,S,T)*100

print(money)

