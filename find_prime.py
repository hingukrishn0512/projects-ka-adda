# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=  i
#     return result

# number = int(input("enter your number : "))
# if(number<0):
#     print("enter positive number ")

# else:
#     print(f"the factorial of the number you enterd is {factorial(number)}")




a = int(input("Enter the number: "))

if a <= 1:
    print("It's not a prime number")
else:
    for i in range(2, int(a**0.5) + 1):  # check divisibility from 2 to sqrt(a)
        if a % i == 0:
            print("It's not a prime number")
            break
    else:
        print("It's a prime number")

