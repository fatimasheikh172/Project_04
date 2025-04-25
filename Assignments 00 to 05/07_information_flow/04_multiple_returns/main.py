def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Tuple packing

def main():
    user_data = get_user_data()  # Tuple unpacking can also be done here if needed
    print("Received the following user data:", user_data)


if __name__ == '__main__':
    main()