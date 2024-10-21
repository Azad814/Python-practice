stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}  



for stock, price in stocks.items():
    sum =0
    for pri in price:
        sum = sum + pri
    sum = sum/len(price)
    print(f"{stock}==>{price}++> avg: ", round(sum, 2))

s = input("enter the stock to add: ")
p = input("enter the price of the stock: ")
if s in stocks:
    stock[s].append(p)
else:
    stock[s]=[p]
    