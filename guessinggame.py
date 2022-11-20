import random
rannumber = random.randint(1, 10)
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input("Make a guess: "))
    guess_count += 1
    if guess_count == guess_limit:
        print(f"You failed after {guess_count} attempts")
    elif guess < rannumber:
        print(f"Guess too low, you made {guess_count} attempts")
    elif guess > rannumber:
        print(f"Guess too high, you made {guess_count} attempts")

        break
    else:
        print(f"Exactly right you made {guess_count} attempts")

print("Game ends!")