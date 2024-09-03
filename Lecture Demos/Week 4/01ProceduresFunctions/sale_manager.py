sales = []
costPerSale = 10

def addSale(x):
    sales.add(x)

def isProfitable():
    gross = 0
    for sale in sales:
        gross += sale
    loss = len(sales) * costPerSale
    isProfitable = gross > loss
    return isProfitable

def makeProfitable():
    costPerSale -= 1