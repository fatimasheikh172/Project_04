max_length = 3

def shorten(lst):
    # Remove elements from the end until the list is MAX_LENGTH long
    while len(lst) > max_length:
        removed_item = lst.pop()  # Remove the last item
        print(removed_item)  

def main():
    # Example list (you can change this to test with other lists)
    lst = input("Enter the list of values (comma-separated): ").split(",")
    
    # Call the shorten function
    shorten(lst)
    
    print("Final list:", lst)


if __name__ == '__main__':
    main()
