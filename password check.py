a = input("enter your name : ")
b = input("enter your password : ")


c = input("confirm your name :")
d = input("confirm your password : ")


if (a !=c):
    print("name is not matching ")

elif(b!=d):
    print("password is not matching")

else:
    print(f"your name and password you entered is {a} and {b}")