print("welcome to the email slicer")

def slicer():
    email = input("enter your email : ")

    if "@" and "." not in email:
        print("enter valid email" )
    else:
        username = email.split("@")[0]
        domain = email.split("@")[1]

    print(f"your email is {email} ")
    print(f"your username is {username} ")
    print(f"your domain is {domain} ")
    print(f"thanks for coming have a nice day")

slicer()


        

