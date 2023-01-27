hour, minute = map(int, input().split())
cooking = int(input())

plushour = (minute + cooking) //60
minute = (minute + cooking) % 60
if (plushour + hour > 23):
  hour = plushour +hour-24
else:
  hour = plushour +hour
print(hour, minute)


