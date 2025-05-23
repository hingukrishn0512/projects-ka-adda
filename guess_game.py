import random

random_choice= random.randint(1,100)

a = 1
guess =0

while a !=random_choice:
    a = int(input("enter the number :  "))
    guess =+1
    if a > random_choice:
        print("enter smaller ")
    elif a < random_choice:
        print("enter greater ")
    else:
        print("you got me damm")











