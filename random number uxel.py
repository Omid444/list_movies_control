import random

def user_guess():
    attempt = 3
    while attempt > 0:
        user_guess_input = int(input(f"You have {attempt} more guess the number: "))
        #return value to the result var and then print it
        result = random_guess_game(user_guess_input)
        print(result)
        #after the result as required must follow dice
        dice_number = dice()
        print(f"Dice is: {dice_number}")
        #if dice bigger than 5 just print a message
        if dice_number >= 5:
            print("You won one more attempting!")
        #if lower than 5 then make minus -1 from attempt
        else:
            attempt -= 1

def dice():
    return random.randint(1,6)

def random_number():
    return random.randint(1,9)

def random_guess_game(user_input):
    random_num = random_number()
    if user_input == random_num:
        return f"You have guess: {user_input} and the number is: {random_num}\n Yes you WON!!"
    else:
        return f"You have guess: {user_input} and the number is: {random_num}\n You lost! :("



print("This is the game you have to guess the number between 1 - 9, you have 3 attempts")


user_guess()