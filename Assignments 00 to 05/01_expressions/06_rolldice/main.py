import random  

def main():
    # Simulate rolling the first die
    die1 = random.randint(1, 6)

    # Simulate rolling the second die
    die2 = random.randint(1, 6)

    # Calculate the total of both dice
    total = die1 + die2

    
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")


if __name__ == '__main__':
    main()
