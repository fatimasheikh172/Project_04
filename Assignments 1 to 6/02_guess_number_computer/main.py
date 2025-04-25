def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print(f"Think of a number between 1 and {x} and I'll try to guess it!")

    while feedback != 'c':
        if low != high:
            guess = (low + high) //2
        else:
                guess = low  # only one number left
        
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! I guessed your number, {guess}, correctly!")

# Run the game
computer_guess(100)