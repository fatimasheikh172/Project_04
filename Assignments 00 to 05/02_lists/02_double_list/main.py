def double_numbers(numbers):
    # Use list comprehension to double each number
    return [num * 2 for num in numbers]

def main():
    numbers = [6 , 9 , 23 , 56]
    doubled = double_numbers(numbers)
    print("Doubled numbers:", doubled)



if __name__ == '__main__':
    main()
