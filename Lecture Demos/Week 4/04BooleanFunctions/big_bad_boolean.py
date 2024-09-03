# read in values
# if the values are (first 5) prime, then we have a match
#mention that method name kinda sounds like a procedure
def isMatch(num):
    return num in [2,3,5,7,11]

while (num := int(input("Value: "))) != -1:
    if isMatch(num):
        print("Thats a prime!")








# def determine_match(num: int) -> bool:
#     if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
#         return True
#     else:
#         return False

# num = 0
# while (num := int(input("Value: "))) != -1:
#     match = determine_match(num)
#     if match == True:
#         print("Thats prime !")