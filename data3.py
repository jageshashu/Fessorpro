
#keys are always unique
stock_prices={'tsla':1000,'apple':2000,'microsoft':3000,'google':4000}
stock_number={1:'tsla',2:'apple',3:'microsoft',4:'google'}

# Access
v1=stock_prices.get('apple')
print(v1)


#add
a1=stock_prices.update({})