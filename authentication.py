saved_email = 'iano@gmail.com'
saved_password = 'iano'

def user_inputs():
    while True:
        email = input("Enter your email: ")
        email = email.strip().lower()
        if ("@" in email and '.' in email):
            password = input("Enter your password: ")
            break
        else:
            print('Invalid Email')
    return email, password


def check():
    user = user_inputs()
    if (user[0] == saved_email and user[1] == saved_password):
        ans = '\nCongratulations! You are logged in successfully.\n'

        def change():
            chg = input(ans + "Do you want to change the username/password? y/n : ")
            if chg.lower() == 'Y':
                new_email = input("\nPlease enter a new email address: ")
                new_pass = input("Please enter a new password: ")
                saved_email = new_email
                saved_password = new_pass
            else:
                print('okay continue to the next!!!')
            return saved_email, saved_password
    else:
        ans = ('Check your email or password!!!!!')
    return ans
print(check())

def main():
    creds = user_inputs()
    print(f' Your email is: {creds[0]}')
    print(f"Your Password is: {creds[1]}")

main()