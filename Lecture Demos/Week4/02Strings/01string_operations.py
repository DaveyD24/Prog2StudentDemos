#for every entered name, tell me how many D's there are

def dCount(name):
    count = 0
    for c in name.lower():
        if c == 'd':
            count = count + 1
    return count


names = input("Please enter names, separated by a space:")
for name in names.split(' '):
    print(f"D Count for {name} is: {dCount(name)}")







# def dCount(name: str) -> int:
#     count = 0
#     for char in name.lower():
#         if char == 'd':
#             count = count + 1
#     return count

# names = input("Please enter names, seperated by a space:")
# for name in names.split():
#     print(f"D count for {name} is: {dCount(name)}")