def count_numbers(text):
    count = 0

    for char in text:
        if char.isdigit():
            count += 1
            
    print(f"The count of numbers is: {count}")

input_user = input("Enter your text or numbers: ")

count_numbers(input_user)


# char = 'A'
# print(char.isalpha())    # True
# print(char.isdigit())    # False
# print(char.isupper())    # True
# print(char.islower())    # False
# print(char.isalnum())    # True
# print(char.isspace())    # False
