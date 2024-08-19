count = [0,0,0,0,0,0,0,0,0,0]

value = int(input("Value: "))
while value != -1:
    if (value < 100 and value >= 0):
        count[value // 10] = count[value // 10] + 1
    value = int(input("Value: "))

for i in range(0, len(count)):
    print(f"{i}0's: {count[i]}")