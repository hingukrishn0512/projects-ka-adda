def sum(num):
    summation = 0
    for digit in str(num):
        if digit.isdigit():
           summation += int(digit)
    return summation
    
a = (input("enter your string : "))

print(f"the summation of the digits in string is {sum(a)} ")

