# import the library

" We are using hashlib, a built-in Python library, to securely hash passwords."

"Hashing means converting a password into a fixed string of letters and numbers, which cannot be easily reversed. "

import hashlib

# Provided function to hash passwords
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Stored login data 

"It's a dictionary of users and their hashed passwords."
"In a real app, this would come from a secure database."

stored_logins = {
    "user@example.com": "e99a18c428cb38d5f260853678922e03abd833e06c3ba594baf685b3c6ad8c8d",  # hash for 'abc123'
    "test@domain.com": "ba3272be5223ad0a2ec9cfa27688b6da4b4e03b1b8611f0134d2e7b5edba1d50"  # hash for 'password123'
}

# Login function
def login(email: str, password_to_check: str) -> bool:
    # Hash the password to check
    hashed_password = hash_password(password_to_check)
    
    # Check if the email exists in the stored logins and compare the hashes
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    return False

def main():
   
    email = input("Enter your email: ")
    password_to_check = input("Enter your password: ")

    # Check login
    if login(email, password_to_check):
        print("Login successful!")
    else:
        print("Invalid email or password.")


if __name__ == '__main__':
    main()
