import random  

#This function shows how the password is generated using the following characters such as all lower case letters and all uppercase letter it includes all digits and most symbols that are usable

def generate_password():
    #This shows the available characters for password in the given variables
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-"
    
    #This line of code stores all the characters that the user can choose from and how the program creates the code using the available characters
    available_characters = ""
    
    #This line of code asks the user about how many characters long they want the password to be 
    while True:
        length_input = input("Enter the length of the password (1 to 18 characters): ")
        
        if length_input.isdigit():  # This line of code verifies if the input by the user only has digits and not any other characters 
            length = int(length_input)
            if length < 1:
                print("Password length must be at least 1 character. Setting length to 16.")
                length = 16  #change the default to 16 if the user enters 0. Sixteen is the second largest character length for most accounts that require passwords
            elif length > 18:
                print("Password length cannot exceed 18 characters. Setting length to 18.")
                length = 18 #eighteen is the maximum number of characters the code can create a password with 
            break  #If the input by the user is anything besides a number the code displays an error and asks for them to type an avaible option given
        else:
            print("Invalid input. Please enter a number for the length.")
    
    #This asks the user which character types to include in the password, with validation for 'yes' or 'no'
    #Chat GPT was used to fix the invalid input else commands
    while True:
        include_lowercase = input("Include lowercase letters? (yes/no): ").lower()
        if include_lowercase in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    while True:
        include_uppercase = input("Include uppercase letters? (yes/no): ").lower()
        if include_uppercase in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    while True:
        include_digits = input("Include digits? (yes/no): ").lower()
        if include_digits in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    while True:
        include_symbols = input("Include symbols? (yes/no): ").lower()
        if include_symbols in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    #This adds the chosen characters in the code 
    if include_lowercase == "yes":
        available_characters += lowercase_letters
    if include_uppercase == "yes":
        available_characters += uppercase_letters
    if include_digits == "yes":
        available_characters += digits
    if include_symbols == "yes":
        available_characters += symbols
    
    #This part of the code checks if no character type was selected
    if available_characters == "":
        print("Error: You must select at least one character type!")
        return
    
    #This line generate the password using random.choice()
    #W3Schools was used to help decide these .join and .choice tags/strings
    password = "".join(random.choice(available_characters) for _ in range(length))
    
    #This line outputs the generated password
    print("Generated password: " + password)   

#This line runs the password generator function to start the program
generate_password()
#This line generates the password using the commands stated by the user