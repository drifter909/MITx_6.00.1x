# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\Mark\Dropbox\ProgrammingFiles\MITx_6001x_ver2\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += ' _ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ''
    import string
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result += letter
    return result
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    game_won = False
    guesses_remaining = 8

    print "Welcome to the game Hangman!"
    print "I am thinking of a word " + str(len(secretWord)) + " letters long."
    print '-------------' 
    while game_won == False and guesses_remaining > 0:
        
        print "Number of guesses remaining: " + str(guesses_remaining)
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + \
            getGuessedWord(secretWord, lettersGuessed)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            print "Oops!  That letter is not in my word: " + \
            getGuessedWord(secretWord, lettersGuessed)
            lettersGuessed.append(guess)
            guesses_remaining -= 1
        print '-------------' 

        if isWordGuessed(secretWord, lettersGuessed) == True:
            game_won = True
    
    if game_won:
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses.  The word was " + secretWord
            
            




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
