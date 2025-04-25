def num_is_double(num):
    return num * 2

def main():
    user_input = input("Enter the number: ")

      #Convert the input to an integer

    number = int(user_input)

    result = num_is_double(number)

    print("The number is double is" , result)

if __name__ == '__main__':
    main()