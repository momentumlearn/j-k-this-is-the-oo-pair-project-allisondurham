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


def pick_mystery_word():
    word_bank = medium_words
    return random.choice(word_bank)

def pick_a_word():
        word_bank = []
        print(len(random.choice(medium_words))) 
    
    
def split(word):
    return list(word)


mystery_word = pick_mystery_word()
print(mystery_word)
pick_a_word()
print(split(mystery_word))


# print(easy_words)
# print(medium_words)
# print(easy_words)   


# def difficulty_choice
# def pick_mystery_word(difficulty_choice):
#     return random.choice(difficulty_choice)
    

# def split(word):
#     return list(word)


# mystery_word = pick_mystery_word()
# print(mystery_word)

# print(split(mystery_word))