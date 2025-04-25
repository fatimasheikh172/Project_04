def double_number():

    # user input
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print(f"The double of {number} is {number * 2}") # result the number is doubled
        # except error
    except ValueError:
        print("That was not a valid number. Please try again.")

double_number()