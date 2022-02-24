from words_file import words
import random

guesses = 10
userword = ""
word = random.choice(words)
guessed_letters = []
wrong_letters = []

def reveal_letter(guessed_letters,keyword):
    correct_letters = list(keyword)
    for letter in correct_letters:
        if letter not in guessed_letters:
            keyword = keyword.replace(letter,"*")        
    return f"{keyword}"

def game_over():
    if userword == word:
        return f"Well done, you won. The winning wword was {word}"
    else:
        return f"Out of guesses, you lost. The winning word was {word}"   

while(userword!=word and guesses>0):
    print("\n")
    letter = input(f"Guess a letter: ")

    if letter == "reveal":
        print("\n")
        print(f"The wrong letters you've guessed are: \n{wrong_letters}")        

    elif letter in word:
        guessed_letters.append(letter)
        print(f"The letter {letter}, is correct")
        print("\n")
        print(reveal_letter(guessed_letters,word))
        userword = reveal_letter(guessed_letters,word)
    else:
        print(f"\nWrong guess you have {guesses} guesses left, try again\n")
        guesses-=1
        print(reveal_letter(guessed_letters,word))
        wrong_letters.append(letter)


print("\n")
print(game_over())