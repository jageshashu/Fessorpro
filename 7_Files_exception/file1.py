
#text,csv,html,excel

data='this is some import data'

# f1=open('data.txt','w')      # w stand for write mode
# f1.write(data)               # In write mode the file should not need to exist.
# f1.close()

# f2=open('name.txt','r')      # r stand for read mode
# n=f2.read()                  # In read mode the file should exist otherwise it will give error
# f2.close()

# f3=open('demo.txt','a')      # a stand for append mode
# f3.write('tsla\n')
# f3.close()


stock_prices={'AAPL': 150, 'GOOG': 2800, 'MSFT': 300, 'AMZN': 3500, 'TSLA': 700}
print(stock_prices)

# convert Dictionary to List

def get_portfolio(stock_prices:dict)->list:
    portfolio=[]
    while True:

        name=input('Enter stock name: (press q to quit)').upper()

        if name=='Q':
            break

        price=stock_prices.get(name)

        if price is None:
            print('Stock not found. Please try again.')
        else:
            print(f'stock {name} is added to portfolio')
            portfolio.append((name,price))
    return portfolio

portfolio=get_portfolio(stock_prices)
print('portfolio',portfolio)

def save_data(portfolio:list)->None:
    f1=open('portfolio.txt','a')
    for stock,price in portfolio:
        f1.write(stock+'\n')
    f1.close()

save_data(portfolio)


# Convert Dictionary to Dictionary

def get_portfolio(stock_prices:dict)->dict:
    portfolio={}
    while True:

        name=input('Enter stock name: (press q to quit)').upper()

        if name=='Q':
            break

        price=stock_prices.get(name)

        if price is None:
            print('Stock not found. Please try again.')
        else:
            print(f'stock {name} is added to portfolio')
            portfolio.update({  name:price})
    return portfolio

portfolio=get_portfolio(stock_prices)
print('portfolio',portfolio)

def save_data(portfolio:dict)->None:
    f1=open('portfolio.txt','a')
    for stock,price in portfolio.items():
        f1.write(stock+':'+str(price)+'\n')
    f1.close()

save_data(portfolio)



f2=open('name.txt','r')     
n=f2.read()    
f2.close()

with open('name.txt','r') as f2:        # in with block we don't need to close the file explicitly, it will
    n=f2.read()                         # automatically close the file after the block is executed.