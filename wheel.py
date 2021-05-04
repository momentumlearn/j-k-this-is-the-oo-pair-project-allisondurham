import random

fileObject = open("words.txt", "r")
lines = fileObject.readlines()
words = [line[:-1] for line in lines]

short_words = []
medium_words = []
long_words = []

#typetypetype

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

def game_mode_pick(difficulty_choice):
    if difficulty_choice == "1":
        return short_words
    elif difficulty_choice == "2":
        return medium_words
    elif difficulty_choice == "3":
        return long_words

    else: 
        input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:  ")

def pick_a_word():
    #word_bank = [difficulty_choice]
    print(len(word))
    #return word.lower()

def pick_mystery_word(difficulty):
    word_bank = game_mode_pick(difficulty)
    return random.choice(word_bank)

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 8
    print("Let's play Wheel of Fortune!")
    print(tries)
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
           if guess in guessed_letters:
               print("You already guessed the letter", guess)
           elif guess not in word:
               print(guess, "is not in the word.")
               tries -= 1
               guessed_letters.append(guess)
           else:
               print("You are correct!", guess, "is in the word!")
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(word) if letter == guess]
               for index in indices:
                   word_as_list[index] = guess
               word_completion = "".join(word_as_list)
               if "_" not in word_completion:
                   guessed = True
        elif len(guess) == len(word) and guess.alpha():
            if guess in guessed_words:
                print("You already guessed", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word


        else:
            print("Not correct")
        print(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("You are the winner of this episode of Wheel of Fortune!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". You must leave and start over. Better luck next time.")



intro()
choice = difficulty_choice()

mystery_word = pick_mystery_word(choice).lower()

        



def main():
    word = mystery_word
    play(mystery_word)
    pick_a_word()
    print(mystery_word)
    pick_mystery_word(game_mode_pick(difficulty_choice))
    while input("Play Again? (y/n) ").lower() == "y":
        word = pick_a_word()
        play(word)

if __name__ == "__main__":
    main()