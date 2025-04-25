def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print("Number of even numbers:", count)

def main():
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    count_even(numbers)

if __name__ == '__main__':
    main()
