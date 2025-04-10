import random
from time import sleep

dice_count = 1

def rand_number():
    random_number = random.randrange(1, 10)
    return random_number

def player_input():
    player_guess = int(input('please enter a number from 1 to 9: '))
    return player_guess

def player_guessing(count):
    counter = count
    for i in range(count):
        random_number = rand_number()
        print('random number is: ',random_number)
        player_guess = player_input()
        if player_guess == random_number:
           return 'you Won! Congratulation'
        else:
            counter -= 1
            print(f'wrong number try again you have still {counter} chance\n')
    else:
        return 'Sorry You lose try later'

def dice():
    print('Here you can obtain a chance by throwing a dice:')
    sleep(2)
    print()
    dice_number = random.randint(1, 6)
    print('your dice number is: ', dice_number)
    return dice_number

def main():
    print('Welcome to guess number game you have 3 times chance to guess right number')
    result = player_guessing(3)
    if result != 'you Won! Congratulation':
        dice_rand_number = dice()
        if (dice_rand_number == 5 or dice_rand_number == 6) :
            return player_guessing(1)
    print(result)

if __name__ == '__main__':
    main()