def main():

    height = int(input("How tall are you: "))

    minimum_height = 50

    if height >= minimum_height:

        print("You're tall enough to ride!")

    else:

        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()