def password_check():
    x = eval(input("How often should the password be repeated? "))
    a = input("Password?")
    for i in range(x):
        b = input("Repeat Password!")
        if a==b:
            print("True")
        else:
            print("False")
password_check()