import random

def generate_random_numbers(count=5):
    print(f"Here are {count} random numbers between 1 and 50:")
    for _ in range(count):
        print(random.randint(1, 50))

generate_random_numbers()
