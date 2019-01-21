from random import randrange
from time import sleep
import os
from fileHandler import *


def wait():
    sleep(0.5)


print("""
    Hello to Hangman zahir verison
    pleas select your language:
    1:french
    2:english """)

MAX_ATTEMPT = 10
attempt = MAX_ATTEMPT

lang = int(input(">>>"))
# format the word
if lang == 1:
    PATH2 = 'data/liste_francais.txt'
elif lang == 2:
    PATH2 = 'data/english_list.txt'
else:
    print('Error the programme will quite')
    exit(1)

# random line number
line_number = randrange(line_count(PATH2))

# pick the line from file
line = read_line_with_index(PATH2, line_number).upper()

length = len(line) - 1

template = ['_'] * length

# initial message to show

print("".join(template).center(50, '*'))
print('number of letters is : ', length)
given_letter = set('')
while template.count('_') > 0:
    wait()
    letter = input('guess your letter : \t').upper().strip()
    print()
    if letter in template:
        print('world already exist')
    elif letter in line:
        i = 0
        for i in range(length):
            if line[i] == letter:
                template[i] = letter
        print("".join(template))
    else:
        if letter not in given_letter:
            attempt -= 1
            print(f'Incorrect : {attempt} attempt left')
            given_letter.add(letter)
        else:
            print(f'{letter} already exist')
        if attempt == 0:
            break

if attempt > 0:
    print(f'congratulation you found : {line}')
else:
    print('max attempt reached ...you loose ')
    print(f'the word was {line}')

os.system('pause')
