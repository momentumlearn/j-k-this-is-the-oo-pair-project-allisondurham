
import random

def pick_mystery_word():
    word_bank = ["tiger", "clover", "fork", "cloud"]
    return random.choice(word_bank)
    

def split(word):
    return list(word)


mystery_word = pick_mystery_word()

print(mystery_word)
print(split(mystery_word))