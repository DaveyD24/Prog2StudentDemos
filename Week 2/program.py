#Every pattern
def isAllPassing(marks: list) -> bool:
    for mark in marks:
        if mark < 50:
            return False
    return True

#Any pattern
def anyHighAcheivers(marks: list) -> bool:
    for mark in marks:
        if mark == 100:
            return True
    return False

marks = [87, 76, 75, 85, 60, 51, 49, 50, 89, 100, 94, 82, 80, 91, 67]

#Compute sum
sum = 0
for mark in marks:
    sum = sum + mark

#Compute Average
average = sum / len(marks)

#Print Results
print("Average Mark: " + str(average))
print("100% Pass Rate" if isAllPassing(marks) else "Below 100% Pass Rate")
print("Someone Achieved 100" if anyHighAcheivers(marks) else "No High Achievers")