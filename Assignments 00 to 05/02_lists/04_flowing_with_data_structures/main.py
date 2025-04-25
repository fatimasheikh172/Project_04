def add_three_copies(my_list, data):
   
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    #  input from the user
    message = input("Enter a message to copy: ")
    
    
    my_list = []
    
    
    print("List before:", my_list)
      
    add_three_copies(my_list, message) 
  
    print("List after:", my_list)


if __name__ == '__main__':
    main()
