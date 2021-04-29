import random
# create wheel of fortune game
# computer will randomly choose from a [] of words/must use .lower
# display number of letters in word for user
# for players turn, 1 guess per turn 
# create while loop for player's turn 
# if letter is guessed correctly, print letter
# elif, print "Wrong. Guess again"


class Game:
    def choose_difficulty():
        difficulty_choice = [easy, medium, hard]
        input()
        return choice

    def pick_a_word():
        word_bank = ["tiger", "clover", "fork", "cloud"]
        print(len(random.choice(word_bank)))
        # return answer
        # print(answer)

class Player:
    def round():
        pass
    def guess():
        while answer != True: #for max 8 guesses
            if guess == correct_letter:
                print()#display blank spaces other than correct letter guessed)
            elif guess != correct_letter:
                print("Wrong. Guess Again") #ask for input
            elif guess == repeat_guess:
                print("Letter guessed. Go again")
            elif guess == too_many_letters:
                print("Too many letters")  
            else:
                print("You Broke It!") 


def win_or_lose:
    reveal the answer
    input("do you want to play again")
    #if yes run new game

    

Game.pick_a_word()