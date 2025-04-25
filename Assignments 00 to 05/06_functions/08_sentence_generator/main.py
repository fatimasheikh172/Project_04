 #"This function is responsible for creating and printing a sentence based on the input word and part of speech."

def make_sentence(word, part_of_speech):
    "Check if the part_of_speech is 0 (which means the word is a noun)"
    if part_of_speech == 0:
        # The sentence template for a noun
        # The word is inserted into the sentence at the blank space (____)
        print(f"I am excited to add this {word} to my vast collection of them!")
    
    # Check if the part_of_speech is 1 (which means the word is a verb)
    elif part_of_speech == 1:
        # The sentence template for a verb
        # The word is inserted into the sentence at the blank space (____)
        print(f"It's so nice outside today it makes me want to {word}!")
    
    # Check if the part_of_speech is 2 (which means the word is an adjective)
    elif part_of_speech == 2:
        # The sentence template for an adjective
        # The word is inserted into the sentence at the blank space (____)
        print(f"Looking out my window, the sky is big and {word}!")
    
    # If the user enters a number other than 0, 1, or 2, the input is invalid
    else:
        # The program will print an error message to inform the user of invalid input
        print("Invalid part of speech input. Please enter 0, 1, or 2.")

# Main function to handle user interaction
def main():
    # Prompt the user to enter a word (it can be a noun, verb, or adjective)
    word = input("Please type a noun, verb, or adjective: ")
    
    # Ask the user to specify the part of speech (0 for noun, 1 for verb, 2 for adjective)
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function, passing in the user's word and part_of_speech
    make_sentence(word, part_of_speech)

# This block ensures that the main() function is called when the program is executed
if __name__ == '__main__':
    main()
