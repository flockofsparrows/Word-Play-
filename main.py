### Setup Section ###
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual): 

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
          
        # ...so we'll print it out with a yellow background
          printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
        printColorfulLetter(letter, False, False)
    
    print(Style.RESET_ALL + " ", end="")

# Write a Function that takes in a six-lettered word from the user: def getSixLetterInput()
def getSixLetterInput():
    # Define variable name 'userWord' as the user input and set dummy value
    userWord = ""
    # input validation while loop to prompt user to enter a six character word
    while(len(userWord) != 6):
      userWord = input("Enter a six letter word: ")
    return userWord
### Main Program ###
# Display game title
print(r''' 

____    __    ____  ______   .______       _______     .______    __           ___   ____    ____     __  
\   \  /  \  /   / /  __  \  |   _  \     |       \    |   _  \  |  |         /   \  \   \  /   /    |  | 
 \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  |   |  |_)  | |  |        /  ^  \  \   \/   /     |  | 
  \            /  |  |  |  | |      /     |  |  |  |   |   ___/  |  |       /  /_\  \  \_    _/      |  | 
   \    /\    /   |  `--'  | |  |\  \----.|  '--'  |   |  |      |  `----. /  _____  \   |  |        |__| 
    \__/  \__/     \______/  | _| `._____||_______/    | _|      |_______|/__/     \__\  |__|        (__) 
                                                                                                       
      ''')
print()
# Include a friendly welcome message and instructions
print("Welcomed to Word Play!")
print("======================")
print("~ You have six tries to get the word correct.")
print("~ The word is SIX CHARACTERS long, and you MUST enter a word of this length for each guess.")
print("~ If a letter is in the CORRECT PLACE, it will be green.")
print("~ If a letter is in the word but NOT in the correct place, it will be yellow.")
print("~ If the letter is NOT in the word at all, it will be red.")
# Create secret word and equate it with variable 'actual'
actual = "virtue"
# Create a variable to keep track of number of guesses & set to 0
numberOfGuesses = 0
# Create variable name for user input and set value to ""
userInput = ""
# while loop to run untill they guess the secret word or use their alotted six turns & prompt user to enter a six letter word. 
while (userInput != actual and numberOfGuesses != 6):
  userInput = input("Enter a six letter word: ")
  # use the accuracy function that will display word in color with correct variables in the (,) 
  printGuessAccuracy(userInput, actual)
  print()
  # keep track of each iteration by adding each time   
  numberOfGuesses += 1
# if statement for when user might correctly guess & display "You win!"    
if(userInput == actual):
  print("You win!")
# else statement to be displayed if did not guess correctly 
else:
  print("You lost!")
 