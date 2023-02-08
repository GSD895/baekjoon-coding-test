num=(input())
digit = [int(x)for x in num]
print(''.join(map(str,sorted(digit, reverse=True))))

