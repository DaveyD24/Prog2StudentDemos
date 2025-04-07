num = 784

firstDigit = num // 100
middleDigit = (num // 10)%10
finalDigit = num % 10

print(f"{firstDigit}{middleDigit}{finalDigit}")