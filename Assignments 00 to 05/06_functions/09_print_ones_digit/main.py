"""
This function takes an integer 'num' as input.
It calculates and prints the ones digit of the number

"""
def print_one_digit(num):

    """
    We use abs(num) to make sure the number is positive.
    This is important if the input is a negative number, like -42.
     abs(-42) gives 42, so we can still get the correct ones digit.
    """
    ones_digit = abs(num) % 10
    print("The one digit is" , ones_digit) #The % (modulo) operator returns the remainder when divided by 10.

def main():
    "Ask the user to enter a number and convert the input to an integer"
    
    num = int(input("Enter a number:"))
    print_one_digit(num)

if __name__ == '__main__':
    main()