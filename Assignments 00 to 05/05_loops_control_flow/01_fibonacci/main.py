def main():
    number = 1000  
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Print Fibonacci numbers until the next number exceeds MAX_VALUE
    while a <= number:
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Move to the next Fibonacci numbers

if __name__ == '__main__':
    main()
