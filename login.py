import re
username_patter = "^[a-z]+[a-zA-z0-9]+[@]{1}[a-z]+[.]{1}[a-z]{3}"
pass_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%&*?])[A-Za-z0-9@#$%&*?]{5,16}$"
def isValidemail(user_name):
    if re.fullmatch(username_patter, user_name):
        return True
    else:
        return False

def isValidpwd(pass_word):
    if re.fullmatch(pass_pattern, pass_word):
        return True
    else:
        return False


def register():
    f = open("dbase.txt", "r")
    u = []
    p = []
    for i in f:
        a, b = i.split(",")
        u.append(a)
        p.append(b)
    
    user_name = input("enter your name:")
    if isValidemail(user_name):
        pass_word = input("enter your password:")
        if isValidpwd(pass_word):
            f = open("dbase.txt", "a")
            f.write(user_name+','+pass_word+"\n")
            print(" registration successful")
            main()
        else:
            print("\n invalid password,please try again..")
            register()
    else:
        print("\n invalid username,please try again..")
        register()


def login():
    f = open("dbase.txt", "r")
    u = []
    p = []
    for i in f:
        a, b = i.split(",")
        u.append(a)
        b = b.strip()
        p.append(b)

    userName = input("\n please enter your username:")
    if userName in u:
        passWord = input("\n please enter your password:")
        if passWord in p:
            print("\n login successful..")
        else:
            print("\n password do no match,please try again.." )
            main()
    else:
        print("\n invalid username,plz try again..")
        login()



def forgotpwd():
    f = open("dbase.txt", "r")
    u = []
    p = []
    for i in f:
        a, b = i.split(",")
        u.append(a)
        b = b.strip()
        p.append(b)
    file = open("dbase.txt", "r")
    lines = file.readlines()
    u_name = input("\nplease enter your user name:")
    if u_name in u:
        new_password = input("\nplease enter new password:")
        if isValidpwd(new_password):

            file = open("dbase.txt", "w")
            for line in lines:
                data = line.split(",")
                if data[0] == u_name:
                    data[1] = str(new_password) + "\n"
                    file.write(",".join(data))
                else:
                    file.write(line)
            file.close()
        else:
            print("\n enter a valid password")
            forgotpwd()
    else:
        print("\n username does not exists")
        main()

def main():
    print('''\n choose an options"
          Register=1,
          login=2,
          reset_password=3,''')
    option = int(input("enter your option:"))
    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        forgotpwd()
    else:
        print("\n choose valid option")
        main()

main()



