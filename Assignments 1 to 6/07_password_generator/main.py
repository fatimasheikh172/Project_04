import random
import string

def generate_strong_password(length=12):
    if length < 6:
        return "Password should be at least 6 characters long."

    # At least one letter, digit, and symbol
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill remaining length
    remaining_length = length - len(password)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=remaining_length)

    # Shuffle to make it unpredictable
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("🔐 Strong Password:", generate_strong_password(12))
