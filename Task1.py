import re

def user_Validation(email):

    pattern="^[A-Za-z][A-Za-z0-9-.]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    result=re.match(pattern,email)

    if result:
        wfp=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","a")
        id=email+" "
        wfp.writelines(id)
        return result
    else:
        print("User name doesn't meet expected security levels, try again")
        registration_validation() 

def password_Validation(passcode):

    pattern2="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$"
    result_p=re.match(pattern2,passcode)

    if result_p:
        wfp=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","a")
        id=passcode+"\n"
        wfp.writelines(id)
   
    else:
        print("Your password doesn't meet expected security levels")
        re_entering_password=input("Your password should be in 5 to 16 digits and contains at least one capital letter, one specails char and one digit: " )
        password_Validation(re_entering_password)

def registration_validation():

        username=input("Enter your user name : ")
    
        rfp2=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","r")
        list_of_data=rfp2.readlines()
        usersList=[]
        passcodeList=[]
        for x in list_of_data:
            u,p=x.split()
            usersList.append(u)
            passcodeList.append(p)

        if username not in usersList:
            
                is_userValid = user_Validation(username)
                if is_userValid:
                    password=input("Enter your password : ")
                    password_Validation(password)
        else:
            print(username+" "+"already exist")

def login_Validation():

    email=input("Enter your registered username or email: ")
    uList=[]
    pList=[]
        
    rfp1=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","r")
    l=rfp1.readlines()

    for x in l:
        u,p=x.split()
        uList.append(u)
        pList.append(p)

    if email in uList:
        
        for line in l:
                
            u,p=line.split()

            if email == u:

                pass_word=input("Enter your password: ")
                    
                if pass_word==p:
                        print("Login is sucessful!")
                else:
                        print("Entered password is incorrect, try again")
                break
    else:   
        print(email+" isn't registered. Please register before you login")
 
def forgot_password():
    
    reg_user=input("Enter your registered email or username: ")

    rfp2=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","r")
    list_of_data=rfp2.readlines()
    
    u_List=[]
    p_List=[]
    reg_U=""

    for x in list_of_data:
        u,p=x.split()
        u_List.append(u)
        p_List.append(p)

    if reg_user in u_List:
        for i in range(0,len(list_of_data)):

            reg_U,saved_Pword = list_of_data[i].split()

            if reg_user == reg_U:
                try:
                    user_choice=input("Enter 1 to recover your password, 2 for updating your password: ").split()
                    a=list(map(int,user_choice))
                    b=a[0]
                except:
                    print("Wrong input, enter integers only.")
                else:
                    if b==1:
                        print("user: " +reg_U)
                        print("Saved Password: "+saved_Pword)
                        break
                    elif b==2:
                        wfp2=open("C:/Data Science/Assignments/Task 1/User_and_Passcodes.txt","w")
                        updated_Pword=reset_Password()
                        list_of_data[i]=reg_user+" "+updated_Pword
                        wfp2.writelines(list_of_data)
                        print("Yours updated Password: "+updated_Pword)
                        break
                    else:
                        print("Wrong input, enter either 1 or 2 only.")
                        break
    else:
        print(reg_user+" doesn't exist, please register.")

def reset_Password():
    
    new_Pword=input("Type your new password: ")

    pattern2="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$"
    result_new_p=re.match(pattern2,new_Pword)

    if result_new_p:
        id = new_Pword+"\n"
        
    else:
        print("Not a valid password,try again")
        forgot_password()

    return id

try:
    choice=input("Enter 1 for registration, 2 for login, 3 for forgot password: ").split()
    choice=list(map(int,choice))
except:
    print("Wrong input, enter integers only.")
else:
    if choice[0]==1:
        registration_validation()
    elif choice[0]==2:
        login_Validation()
    elif choice[0]==3:
        forgot_password()
    else:
        print("Wrong input, please enter 1 or 2 or 3 only")   