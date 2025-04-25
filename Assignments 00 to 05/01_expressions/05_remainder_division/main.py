def main():
    # Ask the user for the number to be divided
    dividend = int(input("Please enter an integer to be divided: "))

    # Ask the user for the number to divide by
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

   
    print(f"\nThe end of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
