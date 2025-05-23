import random

rock = 1
paper = 2
scissors = 3

def game():
    print("Hope you enjoy the game!")
    print("rock = 1, paper = 2, scissors = 3")

    a = int(input("Enter your choice (1/2/3): "))
    
    if a not in [1, 2, 3]:
        print("❌ Enter a valid number (1, 2, or 3)")
        return  # exit the function early

    l1 = [rock, paper, scissors]
    random_number = random.choice(l1)

    print(f"Computer chose: {random_number}")

    if a == random_number:
        print("🤝 It's a tie!")
    elif (a == 1 and random_number == 3) or (a == 2 and random_number == 1) or (a == 3 and random_number == 2):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

game()
