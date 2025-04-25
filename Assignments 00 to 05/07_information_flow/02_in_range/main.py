def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Get three numbers from the user
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    # Call the in_range function and print the result
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()