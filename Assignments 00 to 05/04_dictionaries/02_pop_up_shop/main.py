def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 2.5,
        "durian": 5.0,
        "jackfruit": 3.0,
        "kiwi": 4.0,
        "rambutan": 6.5,
        "mango": 3.5
    }
    
    total_cost = 0  # Variable to store the total cost
    
    # Loop through the fruit prices dictionary
    for fruit, price in fruit_prices.items():
        # Prompt user for quantity of each fruit
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        
        # Calculate the cost for the current fruit and add it to total_cost
        total_cost += quantity * price
    
   
    print(f"Your total is ${total_cost:.2f}")


if __name__ == '__main__':
    main()
