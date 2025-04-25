def main():
    # 1 foot = 12 inches
    per_inches_foot = 12

    #  user to enter a value in feet
    user_input = input("Enter length in feet: ")

    # Convert the input to a float (so it works for decimals too)
    feet = float(user_input)

    # Calculate the equivalent inches
    inches = feet * per_inches_foot

   
    print(f"\n{feet} feet is equal to {inches} inches.")



if __name__ == '__main__':
    main()
