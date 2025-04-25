def main():

    age = int(input("Enter your age: "))

    "Define the voting ages for each fictional country"

    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48

    "Check voting eligibility for each country"

    if age >= peturksbouipo_age:
        
        print("you are eligible to vote in peturksbouipo age")

    else:
        print("your are not eligible to vote!")

    if age >= stanlau_age:

        print("You meet the voting age for Stanlau!")
    
    else:
        print("You can't vote in Stanlau yet. Hang in there!")

    if age >= mayengua_age:

        print("Awesome! You can vote in Mayengua.")

    else:

        print("Not quite there for Mayengua. Maybe in the future!")


if __name__ == '__main__':
    main()