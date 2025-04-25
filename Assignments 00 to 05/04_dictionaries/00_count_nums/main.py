def main():
    # Create an empty dictionary to store the count of each number
    number_counts = {}

    # Infinite loop to keep asking for numbers
    while True:
        # Ask the user for input
        num = input("Enter a number (or 'done' to stop): ")

        # If the user types 'done', stop the loop
        if num.lower() == 'done':
            break

        # Convert the input to an integer
        num = int(num)

        # Update the count of the number in the dictionary
        if num in number_counts:
            number_counts[num] += 1
        else:
            number_counts[num] = 1

   
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")


if __name__ == '__main__':
    main()
