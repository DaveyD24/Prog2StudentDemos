class Program:

    #Every pattern
    def isAllPassing(marks: list) -> bool:
        for mark in marks:
            if mark < 50:
                return False
        return True

    #Any pattern
    def anyHighAchievers(marks: list) -> bool:
        for mark in marks:
            if mark == 100:
                return True
        return False

    if __name__ == "__main__":
        marks = [87, 76, 75, 85, 60, 51, 49, 50, 89, 100, 94, 82, 80, 91, 67]

        #Compute sum
        sum = 0
        for mark in marks:
            sum += mark

        #Compute Average
        average = sum / len(marks)

        #Print Results
        print(f"Average Mark: {average:.2f}")
        print("100% Pass Rate" if isAllPassing(marks) else "Below 100% Pass Rate")
        print("Someone Achieved 100" if anyHighAchievers(marks) else "No High Achievers")