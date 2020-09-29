import random

guessedletters = []
lives = 6
words = ['HELLO','WHATEVER','EXCITEMENT','EVAPORATE','ROLLERCOASTER','MOUNTAINS','SUPERCALIFRAGILISTICEXPIALIDOCUS']
def addLetter(letter):
    for i in range(len(guessedletters) - 1):
        if letter == guessedletters[i]:
            return "Letter already guessed."
    guessedletters.append(letter)
    return "..."

def PrintWord(word):
    for i in range(len(word)):
        for j in range(len(guessedletters)):
            if word[i] == guessedletters[j]:
                print(word[i], end=' ')
        print("_", end = ' ')



print("Welcome to Hangman!")
word = random.choice(words)

while True:
    PrintWord(word)
    letter = input("\n Guess Letter:")
    print(addLetter(letter))
