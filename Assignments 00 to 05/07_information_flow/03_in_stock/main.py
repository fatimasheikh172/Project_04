# This function returns how many of a given fruit are in stock.
def num_in_stock(fruit):
    inventory = {
        'apple': 50,
        'banana': 30,
        'pear': 1000,
        'orange': 20
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    quantity = num_in_stock(fruit)

    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")


if __name__ == '__main__':
    main()
