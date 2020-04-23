import random


level = input("Welcome to the guessing game\n select a level you want to play\n between Hard(H), Medium(M) and Easy(E): ")


while (level == "E"):
    print("Guess a number between 1 and 10")
    print("You have only 6 chances for this level (EASY)")
    secret_number = random.randint(1, 10)
    guess_limit = 6
    guess_count = 0
    
    while(guess_limit > 0):
        user_guess = int(input("Take a wild guess : "))
        guess_limit -=1
        guess_count +=1


        if user_guess > secret_number and guess_count != 6 :
            print(user_guess , " is wrong and is too high")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess < secret_number and guess_count != 6:
            print(user_guess , " is wrong and is too low")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess != secret_number and guess_count == 6:
            print(user_guess , " is the wrong answer and you are out of guesses")
            print("GAME OVER!!!")
            break
        else:
            print("You got it right ", user_guess , " is the correct answer.")
            print("YOU WIN!!!")
            break
    break


while (level == "M"):
    print("Guess a number between 1 and 20")
    print("You have only 4 chances for this level (MEDIUM)")
    secret_number = random.randint(1, 20)
    guess_limit = 4
    guess_count = 0
    
    while(guess_limit > 0):
        user_guess = int(input("Take a wild guess : "))
        guess_limit -=1
        guess_count +=1


        if user_guess > secret_number and guess_count != 4 :
            print(user_guess , " is wrong and is too high")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess < secret_number and guess_count != 4:
            print(user_guess , " is wrong and is too low")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess != secret_number and guess_count == 4:
            print(user_guess , " is the wrong answer and you are out of guesses")
            print("GAME OVER!!!")
            break
        else:
            print("You got it right ", user_guess , " is the correct answer.")
            print("YOU WIN!!!")
            break
    break


while (level == "H"):
    print("Guess a number between 1 and 50")
    print("You have only 3 chances for this level (MEDIUM)")
    secret_number = random.randint(1, 50)
    guess_limit = 3
    guess_count = 0
    
    while(guess_limit > 0):
        user_guess = int(input("Take a wild guess : "))
        guess_limit -=1
        guess_count +=1


        if user_guess > secret_number and guess_count != 3 :
            print(user_guess , " is wrong and is too high")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess < secret_number and guess_count != 3:
            print(user_guess , " is wrong and is too low")
            print("You have ", guess_limit , " guess(es) remaining")
            continue
        elif user_guess != secret_number and guess_count == 3:
            print(user_guess , " is the wrong answer and you are out of guesses")
            print("GAME OVER!!!")
            break
        else:
            print("You got it right ", user_guess , " is the correct answer.")
            print("YOU WIN!!!")
            break
    break


