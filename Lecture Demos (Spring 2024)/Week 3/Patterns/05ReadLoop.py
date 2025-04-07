#Read Pattern (for integer)
#var = int(input("<label>"))

#Read Loop Pattern
# <read pattern>
# while <value> != <end value>:
#     <use the value>
#     <read pattern>

# total = 0
# num = int(input("Number:"))
# while num != -1:
#     total += num
#     num = int(input("Number:"))

# #Verify using output pattern
# print(f"The total is {total}")



#Array Loop example
sales = [100.0, 201.0, 205.5]

# profit = 0
# for sale in sales:
#     profit += sale
# print(f"Total Profit: {profit}")

profit = 0
for i in range(len(sales)):
    print(f"Adding Sale Number {i + 1}...")
    profit += sales[i]
    print("Added!")
print(f"Total Profit: {profit}")
