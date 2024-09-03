sales = [102.3, 48, 294.8, 0.0, 86.5, 417.7, 166.4]

# profit = 0
# for sale in sales:
#     profit += sale
# average = profit / len(sales)
# print(f"Profit: {profit}, Average sale: %.3f" %average)

profit = 0
for i in range(len(sales)):
    profit += sales[i]
    print(f"Successfully added sale {i + 1}")
average = profit / len(sales)
print(f"Profit: {profit}, Average sale: %.3f" %average)