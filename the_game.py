import random
from words import word_list
from hangman_art import logo, stages

def take_a_word():
    word = random.choice(word_list).upper()
    return word

def player():
    print(logo)
    word = list(take_a_word())
    blanks = ['_' for _ in range(len(word))]

    life = 6
    win = False

    while life > 0 or win == True:

        if blanks == word:
            win = True
            print('You won')
            break

        print(blanks)

        user_input = input('Guess a letter: ').upper()
    
        for i in range(len(blanks)):

            if user_input in word[i]:
                blanks[i] = user_input
            elif user_input not in word:
                life -= 1
                print(stages[life])
                break
            else:
                continue
    
    if life == 0:
        print('You lose')


player()
