def main():
    # speed of light constant
    C = 299_792_458  # in meters per second
    
    while True:
        try:
            # Ask user for mass input
            mass_input = input("Enter kilos of mass (or type 'exit' to quit): ")
            
            if mass_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            m = float(mass_input)  # Convert input to float (mass in kg)

            # Calculate energy using E = m * C^2
            E = m * (C ** 2)

            # Output the results
            print("\ne = m * C^2...\n")
            print(f"m = {m} kg")
            print(f"C = {C} m/s")
            print(f"{E} joules of energy!\n")
        
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()
