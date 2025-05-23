def fibonacci(n):
    a , b =0 ,1
    print("fibonacci series")
    for i in range (n):
        print(a , end=" ")
        a , b = b,a+b   # aane aamaj lakhay dhyan rakhje

# Get user input
num = int(input("Enter how many terms you want: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    fibonacci(num)
