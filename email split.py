email = input("enter your email : ")

username = email.split("@")[0]

domain = email.split("@")[1]

print (f"your username is {username} and the domain is {domain}")


