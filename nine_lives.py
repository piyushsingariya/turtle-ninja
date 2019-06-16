import random

words = ['pizza', 'fairy', 'teeth', 'shirt', 'other', 'archy']
secret_word = random.choice(words)
difficulty = input("Choose diifculty, Type 1, 2 or 3 :\n 1 == Easy\n 2 == Normal\n 3 == Hard\n")
difficulty = int(difficulty)

if difficulty == 1:
    lives = 9
elif difficulty ==2:
    lives = 6
else:
    lives = 3
clue = list('?????')
heart_symbol = u'\u2764'
#print (heart_symbol)
guessed_word_correctly = False

def update_clue(guessed_word, secret_word, clue):
    index = 0
    while index<len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left:'+ heart_symbol*lives)
    print(words)
    guess = raw_input()
    if guess == secret_word:
        guessed_letter_correctly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You loose your life')
        lives -= 1
    
if guessed_word_correctly:
    print('You won! The secret word was', secret_word)
else:
    print("You loose! The secret word was", secret_word)