#!/usr/bin/env python3


def process_chars(param):
    """
    Count the occurences of all characters in a string.
    """

    store_vals={}    
    print("Processing the string you entered....")
    for x in param:
        if x in store_vals:
            #We're incrementiing the counter if the charcater already exists
            store_vals[x] += 1
        else:
            #initialze count to 1 if character is new
            store_vals[x] = 1
        
    #Displaying the character counts    
    print(", ".join(f"{char}: {count}" for char, count in store_vals.items())) 


if __name__ == "__main__":
    store = input("\nPlease enter a string\n")
    process_chars(store)
 
