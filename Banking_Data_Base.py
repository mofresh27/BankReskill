#Banking_Data_Base.py

#create record
#update record
#read record 
#delete record
import os
user_db_path = "DATAX/User_Record"

def create(accountNumber, userDetails):

    completetion_state = False
    try: 
        f= open(user_db_path + str(accountNumber)+ ".txt", "x")
        
    except FileExistsError:
        print('user already exist')
        # delete the already created file, and print out error , then return false 
        
    else: 
        f.write(userDetails);
        completetion_state = True
    finally: 
        f.close();
        return completetion_state

    #creating a file 
    #name of file would be account_number.txt
    #add user details to the file 
    #return true 



def update(accountNumber):
    print("update user reocrd")
    #find user user with account number 
    #overwrite record 
    #fetch content of file 
    #save file


def read(accountNumber):
    print("read user record")
    #find user with account number 
    #fetch content of the file 
    #return true 



def delete (accountNumber): 
    print("delete user record")

    if os.path.exists(user_db_path+ str(accountNumber)+ ."txt"):
        os.remove(user_db_path + str(user_account_number)+ ."txt")

    if os.path.exists
    #find user 
    #delete user record 
    #return true 

def find(accountNumber):
    print("find user")
    #find user record in the data folder 




create(7561429834,["jack", 'jason', 'password12345', 500])