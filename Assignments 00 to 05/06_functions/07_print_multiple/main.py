def print_multiple(message, repeats):
    """
    This is a function definition. It accepts two parameters:
    message: a string that the user wants to print
    repeats: an integer representing how many times to print the message
    """
    for _ in range(repeats):
        
        """
        This is a loop that will repeat the block of code inside it exactly repeats times.
         The underscore _ is used here because we don't need the loop variable — we only care about how many times the loop runs.
         range(repeats) generates a sequence from 0 up to repeats - 1.
        """
        print(message, end=" ")

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)


if __name__ == '__main__':
    main()
