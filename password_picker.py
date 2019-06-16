import random
import string
print("Welcome to Password Picker!")

while True:
    adjectives = ['sleepy', 'slow', 'smelly',
                'wet', 'fat', 'red',
                'orange', 'yellow', 'green',
                'blue', 'purple', 'fluffy',
                'white', 'proud', 'brave']

    nouns = [
        'apple', 'dinosour','ball', 'toaster', 'goat',
        'hammer', 'duck', 'panda'
    ]

    adjective = random.choice(adjectives) # selecting from adjectives
    noun = random.choice(nouns) # selecting from nouns
    number = random.randrange(0, 100) # selecting a number
    special_char = random.choice(string.punctuation) # selecting a special character where puncuation is a constant
    password = adjective + noun + str(number) + special_char
    print("Your new password is: %s") % (password)

    response = input("Would you like to generate another password? Type y or n : ")
    if response == 'n':
        break