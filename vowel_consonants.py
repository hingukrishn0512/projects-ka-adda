def count(text):
    vowels = "aeiou"
    v_count = 0
    c_count = 0

    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            if char.lower() in vowels:  # Convert to lowercase before checking for vowel
                v_count += 1
            else:
                c_count += 1

    print(f"vowels: {v_count}")
    print(f"consonants: {c_count}")

input_user = input("Enter your string: ")
count(input_user)
