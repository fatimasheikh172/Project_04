def divisors(num):
    "This function receives a number num as an argument and prints all the divisors of that number."

    print(f"Here are the divisors of {num}")

    for number in range(1 , num + 1):
        "This loop runs from 1 to num (inclusive), checking every number in that range."
        if num % number == 0:
            """
            This is the core logic. It checks:
             If the remainder when num is divided by number is 0, then number is a divisor of num. 
            """
            print(number , end= "")

def main():
    num = int(input("Enter a number: "))
    divisors(num)

if __name__ == '__main__':
    main()