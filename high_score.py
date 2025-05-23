import random

def game():
    print("Hello there! You are playing a game...")

    score = random.randint(1, 100)

    try:
        with open("read.txt", "r") as f:
            hiscore = f.read().strip()

            if hiscore == "":
                hiscore = 0
            else:
                hiscore = int(hiscore)
    except FileNotFoundError:
        # Handle the case when the file doesn't exist yet
        hiscore = 0

    print(f"Your score is: {score}")
    print(f"High score is: {hiscore}")

    if score > hiscore:
        print("Congratulations! You got a new high score 🎉")
        with open("read.txt", "w") as f:
            f.write(str(score))

game()

 