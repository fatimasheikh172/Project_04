def welcome():
   print("\nWelcome to the maidlibs 🎉📜\n")

def get_inputs():
    adjective = input("Enter the adjective: ")
    place = input("Enter the palce: ")
    sound = input("Enter the sound: ")
    animal = input("Enter the animal: ")
    clothing = input("Enter the clothing: ")
    noun = input("Enter the noun: ")
    verb = input("Enter the verb: ")
    object = input("Enter the object: ")
    adjective2 = input("Enter the adjective2: ")

    return adjective , place, sound , animal ,clothing , noun , verb , object, adjective2
    
def create_story(adjective , place, sound , animal ,clothing , noun , verb , object, adjective2):
    story = f"""

It was a {adjective} day in {place} when I heard a loud {sound} coming from my backyard.
I ran outside and saw a {animal} wearing a {clothing}, holding a {noun}!
Without saying a word, it began to {verb} around the {object} like it was in a circus.
I couldn't believe my eyes — even my sister dropped their popcorn in shock.
Later, we named the creature Mr' wiggly and now it lives in our attic,
teaching us how to juggle bananas every evening.
What a {adjective2} life I live!

"""
    return story


def main():
    welcome()
    adjective , place, sound , animal ,clothing , noun , verb , object, adjective2 = get_inputs()
    story = create_story( adjective , place, sound , animal ,clothing , noun , verb , object, adjective2)
    print("\n📝 Here's your story:\n")
    print("🐾🎩 The Unexpected Visitor 🚪👀")
    print(story)
    print("Thanks for playing! 👋")

    

# Run the game
main()


