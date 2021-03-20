# Enhancements
# When entering character
#    Don't allow same letter more than once - DONE
#    Don't allow symbols or white spaces - DONE
# Allow multiple words - DONE

import glob
import re
from random import randrange

MAX_WRONG_ATTEMPTS = 10
LETTERS_REGEX = re.compile('[A-Z]')

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
attemptedCharacters=[]

currentWord = LETTERS_REGEX.sub("_", wordToGuess)

while(not gameComplete):
    print(f"Incorrect count: {incorrectCounter}")
    print(currentWord)

    letterToGuess = ""
    validLetter = False
    while not validLetter:
        letterToGuess = input("Enter letter to guess [A-Z]: ")
        if letterToGuess.isalpha():
            letterToGuess = letterToGuess[0].upper()
            if letterToGuess in attemptedCharacters:
                print("Letter already attempted!")
            else:
                validLetter = True

    attemptedCharacters.append(letterToGuess)

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

    if incorrectCounter >= MAX_WRONG_ATTEMPTS:
        print(f"Shot by Boggis/Bunce and Bean. Word was: {wordToGuess}")
        gameComplete = True

# url = f"https://wordsapiv1.p.rapidapi.com/words/{wordToGuess}"
#
# headers = {
#     'x-rapidapi-key': f"{WORD_API_KEY}",
#     'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)