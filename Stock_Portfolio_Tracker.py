stock_prices = { #Stores stock names and their prices
    "AAPL": 180,                  
    "TSLA": 250,                  
    "GOOG": 150,                 
    "MSFT": 400,                 
    "AMZN": 180                  
}

total_investment = 0 #Stores total investment

print("Available Stocks:")       

for stock, price in stock_prices.items(): #Gets each stock and its price
    print(stock, ":", "$" + str(price))   

while True:                   

    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE": #Checks if user entered DONE
        break                   

    if stock not in stock_prices: 
        print("Stock not available!")  #Shows error message
        continue                 

    quantity = int(input("Enter quantity: "))

    value = stock_prices[stock] * quantity #Calculates investment = stock price × quantity

    total_investment += value     
    print("Investment in", stock, "=", "$" + str(value)) #Print investment value of the stock

print("\nTotal Portfolio Value = $" + str(total_investment))
print("Thank you!") #Prints final message