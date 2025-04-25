import math  

def main():
    # Ask the user for the lengths of the two perpendicular sides
    xy = float(input("Enter the length of AB: "))
    xz = float(input("Enter the length of AC: "))

    # Use the Pythagorean theorem to calculate the hypotenuse
    bc = math.sqrt(xy ** 2 + xz ** 2)

   
    print(f"\nThe length of BC (the hypotenuse) is: {bc}")


if __name__ == '__main__':
    main()
