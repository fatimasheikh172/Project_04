def get_first_element(lst):
   
    print(lst[0])

def main():
   
    n = int(input("How many elements in the list? "))
    
    lst = []
    
    # Collect the list elements from the user
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)
    
    # Call the function to print the first element
    get_first_element(lst)


if __name__ == '__main__':
    main()
