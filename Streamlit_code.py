import streamlit as st
import re

def user_Validation(email):
    pattern="^[A-Za-z][A-Za-z0-9-.]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    result=re.match(pattern,email)

    if result:
        with open("New_User_and_Passcodes.txt", "a") as wfp:
            id=email+" "
            wfp.writelines(id)
        return result
    else:
        st.error("User name doesn't meet expected security levels, try again")
        registration_validation() 

def password_Validation(passcode):
    pattern2="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$"
    result_p=re.match(pattern2, passcode)

    if result_p:
        with open("New_User_and_Passcodes.txt", "a") as wfp:
            id=passcode+"\n"
            wfp.writelines(id)
    else:
        st.error("Your password doesn't meet expected security levels")
        re_entering_password=st.text_input("Re-enter your password:")
        password_Validation(re_entering_password)

def registration_validation():
    username = st.text_input("Enter your user name:")
    
    with open("New_User_and_Passcodes.txt", "r") as rfp2:
        list_of_data = rfp2.readlines()
    
    usersList = []
    passcodeList = []
    for x in list_of_data:
        u, p = x.split()
        usersList.append(u)
        passcodeList.append(p)

    if username not in usersList:
        is_userValid = user_Validation(username)
        if is_userValid:
            password = st.text_input("Enter your password:")
            password_Validation(password)
    else:
        st.error(f"{username} already exists")

def login_Validation():
    email = st.text_input("Enter your registered username or email:")
    
    uList = []
    pList = []

    with open("New_User_and_Passcodes.txt", "r") as rfp1:
        l = rfp1.readlines()

    for x in l:
        u, p = x.split()
        uList.append(u)
        pList.append(p)

    if email in uList:
        for line in l:
            u, p = line.split()

            if email == u:
                pass_word = st.text_input("Enter your password:")

                if pass_word == p:
                    st.success("Login is successful!")
                else:
                    st.error("Entered password is incorrect, try again")
                break
    else:
        st.error(f"{email} isn't registered. Please register before you login")

def forgot_password():
    reg_user = st.text_input("Enter your registered email or username:")
    
    with open("New_User_and_Passcodes.txt", "r") as rfp2:
        list_of_data = rfp2.readlines()
    
    u_List = []
    p_List = []
    reg_U = ""

    for x in list_of_data:
        u, p = x.split()
        u_List.append(u)
        p_List.append(p)

    if reg_user in u_List:
        for i in range(0, len(list_of_data)):
            reg_U, saved_Pword = list_of_data[i].split()

            if reg_user == reg_U:
                user_choice = st.radio("Enter 1 to recover your password, 2 for updating your password", options=[1, 2])
                if user_choice == 1:
                    st.write(f"user: {reg_U}")
                    st.write(f"Saved Password: {saved_Pword}")
                elif user_choice == 2:
                    updated_Pword = reset_Password()
                    list_of_data[i] = reg_user + " " + updated_Pword
                    with open("New_User_and_Passcodes.txt", "w") as wfp2:
                        wfp2.writelines(list_of_data)
                    st.success(f"Yours updated Password: {updated_Pword}")
                break
    else:
        st.error(f"{reg_user} doesn't exist, please register.")

def reset_Password():
    new_Pword = st.text_input("Type your new password:")

    pattern2 = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$"
    result_new_p = re.match(pattern2, new_Pword)

    if result_new_p:
        return new_Pword
    else:
        st.error("Not a valid password, try again")
        return reset_Password()

# Main function that determines which action to take
def main():
    choice = st.selectbox("Choose an action", options=["Registration", "Login", "Forgot Password"])
    
    if choice == "Registration":
        registration_validation()
    elif choice == "Login":
        login_Validation()
    elif choice == "Forgot Password":
        forgot_password()

if __name__ == "__main__":
    main()
