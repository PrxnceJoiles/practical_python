#!/usr/bin/env python3


def remove_duplicates(my_list):
    """
    This removes duplicates form the list and cretae a tuple.
    It also prints the maximum and the minimum
    """
    
    #This creates a list unique values
    unique_values = tuple(sorted(set(my_list)))  
    
    
    #We're validating the tuple here
    if unique_values: 
        print(f"Unique values: {unique_values}")
        print(f"Minimum: {min(unique_values)}")
        print(f"Maximum: {max(unique_values)}")
    else:
        print("List is empty")

    
if __name__  == "__main__":

   try:
        input_str = input("Please enter a list of integers separated by commas: ")
        stores = [int(x) for x in input_str.split(",")] 
        remove_duplicates(stores)

   #This exceptoion is for non integer values
   except ValueError:
        print("Error: Invalid input. Please enter integers only.")

   #This exceptions catches any other expected errors.
   except Exception as e:
        print(f"Please see the Error: {e}")
