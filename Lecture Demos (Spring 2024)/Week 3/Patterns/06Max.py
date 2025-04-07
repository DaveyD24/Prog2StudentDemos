#Max Pattern
# max1 = <smallest number>
# <for each item>:
#     if <item> > max1:
#         max1 = <item>

nums = [148, 124, 156, 145, 198, 123, 114, 178, 192]

max1 = float('-inf')
for num in nums:
    if num > max1:
        max1 = num

min = float('inf')
for num in nums:
    if num < min:
        min = num

#Verify with output pattern
print(f"Biggest Number: {max1}")
print(f"Smallest Number: {min}")