import random

massive_giant_word_list = open("words.txt", "r")
lines = massive_giant_word_list.readlines()
words = [line[:-1] for line in lines]

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
########################################################################


def intro():
    print()
    line ="""THIS IS WHEEL OF FORTUNE!\n 
            You will have a chance to guess a random word.\n
            Start by guessing a vowel and then a consonant.\n
            You will be given 8 chances to guess the word correctly.\n
            Any letter guessed correctly will display in the blank spaces for the word.\n
            Good luck and have fun!\n"""
    print(line)


def difficulty_choice():
    choice = input("Choose a difficutly:  ENTER  1 for Easy, 2 for Normal, or 3 for Challenging:       ")
    if choice == "1":
        return short_words
    elif choice == "2":
        return medium_words
    elif choice == "3":
        return long_words
    else: 
        print('please choose a valid value')
        return difficulty_choice()
    

def pick_mystery_word(word_bank):
    return random.choice(word_bank)


###########################################################################################


def play(word):
    word_completion = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print("")
    print("Let's play WHEEL OF FORTUNE!")
    print(f'The mystery word has {len(word)} letters.')
    print(f'You have {tries} guesses.')
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Your guess:    ").upper()


        if len(guess) == 1 and guess.isalpha():
           if guess in guessed_letters:
               print("You have already guessed the letter", guess)
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
                   word_as_list[index * 2] = guess
               word_completion = "".join(word_as_list)
               if "_" not in word_completion:
                   guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Please guess a single letter")


        print(f' You have {tries} guesses remaining.')
        print(word_completion)
        print("\n")

    if guessed:
        print("CONGRATS!!!  You are the WINNER of this episode of WHEEL OF FORTUNE!!!")
        print("")
        pass

    else:
        print("Sorry, you ran out of guesses. The word was " + word + ". Better luck next time.")
        print()
        pass


#########################################################################################################


def main():
    intro()
    word_bank = difficulty_choice()
    mystery_word = pick_mystery_word(word_bank).upper()
    word = mystery_word
    print(mystery_word)
    play(word)
    

def play_the_game():
    while True:
        print("")
        yes_no = input("Are you ready to play WHEEL OF FORTUNE?    YES or NO?       ")
        affirm = yes_no.lower()
        if affirm == "yes":
            main()
        elif affirm == "no":    
            print("Goodbye, have a goood day!")
            break
        else: 
            continue


play_the_game()