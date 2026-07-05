
secret_number = 7

game_won = False

for i in range(1,4):
    print (f"\nAttempt {i} of 3")
    guess = int(input("Enter your guess (between 1 and 10): "))
    
    if guess == secret_number:
        print("Congratulations!\t You guessed the correct number.")
        game_won = True
        break
    elif guess > 10 or guess < 1:
        print("Invalid guess")
    else:
        print("Wrong guess. Try again.")

if not game_won:
    print("Game Over. The secret number was:", secret_number)



    