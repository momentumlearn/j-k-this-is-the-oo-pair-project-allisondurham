import random

fileObject = open("words.txt", "r")
lines = fileObject.readlines()
words = [line[:-1] for line in lines]
# print(words)

short_words = []
medium_words = []
long_words = []

for word in words:
    if len(word) == 4 or len(word) == 5:
        short_words.append(word)
        # return short_words
    elif len(word) == 6 or len(word) == 7:
        medium_words.append(word)
        # return medium_words
    elif len(word) >= 8:
        long_words.append(word)
        # return long_words
    else: 
        pass

##################################################
def intro():
    print()
    line ="""THIS IS WHEEL OF FORTUNE!\n 
            You will have a chance to guess a random word.\n
            Start by guessing a vowel and then a consonant.\n
            You will be given 8 chances to guess the word correctly.\n
            The letter guessed correctly will display in the blank spaces for the word.\n
            Good luck and have fun!\n"""
    print(line)

def difficulty_choice():
    user_choice = input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:  ")
    return user_choice

def game_mode_pick(difficulty_choice):
    if difficulty_choice == "1":
        return short_words
    elif difficulty_choice == "2":
        return medium_words
    elif difficulty_choice == "3":
        return long_words
    else:
        input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:  ")    

def pick_mystery_word(difficulty):
    word_bank = game_mode_pick(difficulty)
    return random.choice(word_bank)


def length_of_word(word):
    print(len(word))
    
    
def split(word):
    return list(word)






choice = difficulty_choice()

mystery_word = pick_mystery_word(choice).lower()

intro()

 
print(mystery_word)
length_of_word(mystery_word)
print(split(mystery_word))



############################################



    








