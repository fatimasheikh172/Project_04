def madlib():

    # get the user input

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    place = input("Enter a place: ")


    sentence = f"Today I saw a {adjective} {animal} wearing a {color} hat and dancing at the {place}!"
    print("\nHere's your Mad Lib:\n")

    print(sentence)

    print("\nTHANK YOU")


if __name__ == "__main__":
    madlib()
