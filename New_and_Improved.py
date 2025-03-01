import re

def write_to_file(file_path, data):
    with open(file_path, "a") as f:
        f.writelines(data)

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

def user_Validation(email):
    pattern = "^[A-Za-z][A-Za-z0-9-.]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    result = re.match(pattern, email)
    
    if result:
        write_to_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt", [email + " "])
        return True
    else:
        print("User name doesn't meet expected security levels, try again")
        return False

def password_Validation(passcode):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#?!@$%^&*-]).{5,16}$"
    result_p = re.match(pattern, passcode)
    
    if result_p:
        write_to_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt", [passcode + "\n"])
    else:
        print("Your password doesn't meet expected security levels")
        return False
    return True

def registration_validation():
    username = input("Enter your user name : ")
    
    list_of_data = read_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt")
    usersList = [x.split()[0] for x in list_of_data]

    if username not in usersList:
        if user_Validation(username):
            password = input("Enter your password : ")
            if password_Validation(password):
                print("Registration successful!")
        else:
            registration_validation()  # Retry
    else:
        print(username + " already exists")

def login_Validation():
    email = input("Enter your registered username or email: ")
    list_of_data = read_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt")
    
    usersList = [x.split()[0] for x in list_of_data]
    if email in usersList:
        for line in list_of_data:
            u, p = line.split()
            if email == u:
                pass_word = input("Enter your password: ")
                if pass_word == p:
                    print("Login is successful!")
                else:
                    print("Entered password is incorrect, try again")
                break
    else:
        print(f"{email} isn't registered. Please register before you login")

def forgot_password():
    reg_user = input("Enter your registered email or username: ")
    list_of_data = read_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt")
    
    usersList = [x.split()[0] for x in list_of_data]
    
    if reg_user in usersList:
        for line in list_of_data:
            reg_U, saved_Pword = line.split()
            if reg_user == reg_U:
                while True:
                    try:
                        user_choice = int(input("Enter 1 to recover your password, 2 for updating your password: "))
                        if user_choice == 1:
                            print(f"user: {reg_U}")
                            print(f"Saved Password: {saved_Pword}")
                            break
                        elif user_choice == 2:
                            updated_Pword = reset_Password()
                            list_of_data = [line if line.split()[0] != reg_U else f"{reg_U} {updated_Pword}\n" for line in list_of_data]
                            write_to_file(r"H:\Data Science\Assignments\GUVI\Task 1\New_User_and_Passcodes.txt", list_of_data)
                            print(f"Your updated Password: {updated_Pword}")
                            break
                        else:
                            print("Invalid input, please enter 1 or 2")
                    except ValueError:
                        print("Invalid input, please enter a valid number")
    else:
        print(f"{reg_user} doesn't exist, please register.")

def reset_Password():
    while True:
        new_Pword = input("Type your new password: ")
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#?!@$%^&*-]).{5,16}$"
        if re.match(pattern, new_Pword):
            return new_Pword
        else:
            print("Not a valid password, try again")

def main():
    try:
        choice = int(input("Enter 1 for registration, 2 for login, 3 for forgot password: "))
        if choice == 1:
            registration_validation()
        elif choice == 2:
            login_Validation()
        elif choice == 3:
            forgot_password()
        else:
            print("Invalid input, please enter 1, 2, or 3")
    except ValueError:
        print("Invalid input, please enter integers only.")

if __name__ == "__main__":
    main()
