import random

def main():

    for _ in range(10):
        value = random.randint(1 ,100)  # "Get a random number from 1 to 100"
        print(value, end=' ')  # the number on the same line with a space

        print()

if __name__ == '__main__':
    main()