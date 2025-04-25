
def main():

# Enter the temperature

   fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
   celsius = (fahrenheit - 32.00) * (5.00/9.00)
   print(f"The temperature in Celsius is {celsius:.2f} degrees.")

if __name__ == "__main__":
    main()
