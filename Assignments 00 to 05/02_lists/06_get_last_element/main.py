def get_last_element(lst):
    # Print the last element in the list
    print(lst[-1])

def main():
    # Get the number of elements in the list
    n = int(input("How many elements in the list? "))
    
    lst = []
    
    # Collect the list elements from the user
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)
    
    # Call the function to print the last element
    get_last_element(lst)

if __name__ == '__main__':
    main()
