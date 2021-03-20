# how to play instructions
# enter a word to guess (from a list of words in a file -> randomised)
# display _ for all letters
# enter letters and if you get it wrong update incorrect counter
# if you get it right update the letters _ and display counter
# if incorrect counter hits 10 then system failure, displays the word

# Enhancements
# When entering character
#    Don't allow same letter more than once
#    Don't allow symbols or white spaces
# Allow multiple words
import glob
import re
from random import randrange

filenames = glob.glob("words/*.txt")

for num, filename in enumerate(filenames, start=1):
    wordOption = filename.replace('words/','').replace(".txt","").replace("_", " ").capitalize()
    print(f"{num}: {wordOption}")

wordListOption = int(input("Enter a word list option:"))

with open(filenames[wordListOption - 1]) as f:
    data = f.readlines()

randomElement = randrange(len(data))

gameComplete = False
incorrectCounter = 0
wordToGuess = data[randomElement].upper().strip()

currentWord = ""
for x in range(0, len(wordToGuess)):
    currentWord += "_"

while(not gameComplete):
    print(f"Incorrect count: {incorrectCounter}")
    print(currentWord)

    letterToGuess = ""
    while not letterToGuess.isalpha():
        letterToGuess = input("Enter letter to guess: ")

    letterToGuess = letterToGuess[0].upper()
    found = wordToGuess.find(letterToGuess)
    if found == -1 :
        incorrectCounter+=1
    else: # update the letters in here.
        indexes = [x.start() for x in re.finditer(letterToGuess, wordToGuess)]
        for index in indexes:
            currentWord = currentWord[:index] + letterToGuess + currentWord[index + 1:]

    # Check to see work is complete
    if wordToGuess == currentWord:
        print("Fantastic mr fox")
        gameComplete = True

    if incorrectCounter >=10:
        print(f"Shot by Boggis/Bunce and Bean. Word was: {wordToGuess}")
        gameComplete = True

