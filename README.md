# python-oo-pair-project 🐍 🙌

### Discuss with your partner and choose between the two project options, Wheel of Fortune ⚙️ or Pig 🎲.

## In either case, here are the steps you should follow. Remember to run your code frequently.
1. Read the specs for your project and make sure you both have the same understanding of them.
2. Decide the order of priority for meeting the requirements.
3. Sketch/map out your game.
4. Set up VS Code screen share, so you are both typing in the same VS Code project.
5. From the sketch process, determine what classes you will need. You might find this [list](https://stackoverflow.com/questions/4203163/how-do-i-design-a-class-in-python) helpful.
6. Build each class one at a time.
7. Build the action of the game one step at a time, adding methods to classes as you deem necesary. 

### Word-Based Option: Wheel of Fortune

You will implement the game Wheel of Fortune. In your game, you will have one player.
There will be no wheel, just the letter guessing part.

The computer must select a word at random from the list of words in the file words.txt from this repository.

The game must be interactive; the flow of the game should go as follows:

- Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
- At the start of the game, let the user know how many letters the computer's word contains.
- Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
- Let the user know if their guess appears in the computer's word.
- Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:

`B _ _ B A _ D`

- A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
- A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.
- If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.
- The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.
- When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

_This lab is based off a similar exercise in MIT's 6.00.1x course._

### Number-Based Option: Pig Dice Game

You are going to implement a version of the game of Pig in Python. Here's how the game works.

- Two players are trying to reach 100 points first. 
- On a player's turn, they roll a die over and over until they roll a 1 (a "pig") or they choose to hold. 
- If they hold, they add the sum of their rolls to their score. If they roll a 1, they get no points. 
- After a 1 is rolled or the player holds, the other player takes their turn.
- The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)
- In your implementation, there will be one human player and one computer player. The computer player will always hold until they roll a total of 20 points.

#### Example Game
You do not have to have the same interface or text as this. It is only an example.

```You will be player 2.
Enter nothing to roll; enter anything to hold.
Player 1 score: 0
Player 2 score: 0
It is player 1's turn.
Roll: 5
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 0
It is player 2's turn.
Roll: 6
Turn total: 6 	Roll/Hold? (Enter)
Roll: 5
Turn total: 11 	Roll/Hold? (Enter)
Roll: 6
Turn total: 17 	Roll/Hold? (Enter)
Roll: 2
Turn total: 19 	Roll/Hold? (Enter)
Roll: 2
Turn total: 21 	Roll/Hold? h
Turn total: 21
New score: 21
Player 1 score: 0
Player 2 score: 21
It is player 1's turn.
Roll: 5
Roll: 6
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 21
It is player 2's turn.
Roll: 6
Turn total: 6 	Roll/Hold? (Enter)
Roll: 6
Turn total: 12 	Roll/Hold? (Enter)
Roll: 2
Turn total: 14 	Roll/Hold? (Enter)
Roll: 6
Turn total: 20 	Roll/Hold? h
Turn total: 20
New score: 41
Player 1 score: 0
Player 2 score: 41
It is player 1's turn.
Roll: 3
Roll: 3
Roll: 6
Roll: 4
Roll: 4
Turn total: 20
New score: 20
Player 1 score: 20
Player 2 score: 41
It is player 2's turn.
Roll: 3
Turn total: 3 	Roll/Hold? (Enter)
Roll: 3
Turn total: 6 	Roll/Hold? (Enter)
Roll: 2
Turn total: 8 	Roll/Hold? (Enter)
Roll: 2
Turn total: 10 	Roll/Hold? (Enter)
Roll: 4
Turn total: 14 	Roll/Hold? (Enter)
Roll: 2
Turn total: 16 	Roll/Hold? (Enter)
Roll: 4
Turn total: 20 	Roll/Hold? h
Turn total: 20
New score: 61
Player 1 score: 20
Player 2 score: 61
It is player 1's turn.
Roll: 5
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 61
It is player 2's turn.
Roll: 3
Turn total: 3 	Roll/Hold? (Enter)
Roll: 3
Turn total: 6 	Roll/Hold? (Enter)
Roll: 5
Turn total: 11 	Roll/Hold? (Enter)
Roll: 2
Turn total: 13 	Roll/Hold? (Enter)
Roll: 6
Turn total: 19 	Roll/Hold? h
Turn total: 19
New score: 80
Player 1 score: 20
Player 2 score: 80
It is player 1's turn.
Roll: 3
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 80
It is player 2's turn.
Roll: 2
Turn total: 2 	Roll/Hold? (Enter)
Roll: 2
Turn total: 4 	Roll/Hold? (Enter)
Roll: 4
Turn total: 8 	Roll/Hold? (Enter)
Roll: 2
Turn total: 10 	Roll/Hold? (Enter)
Roll: 3
Turn total: 13 	Roll/Hold? (Enter)
Roll: 6
Turn total: 19 	Roll/Hold? (Enter)
Roll: 5
Turn total: 24 	Roll/Hold? h
Turn total: 24
New score: 104```


