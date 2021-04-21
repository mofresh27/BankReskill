#validationmodule.py

def account_number_validation(accountNumber):
    #check if account number is not empty 
    # if account number is 10 digitis 
    # if the account is a string 
    if accountNumber:
        if len(str(accountNumber)) == 10:
            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Input, Please try again")

        else:
            print("Account number MUST be 10 characters")
            return False 
    
    else: 
        print("Invalid Input")
        return False 

def validation_input(input):
    #check if its a lit 
    #check each item in the list and be usre they are the correct data types 