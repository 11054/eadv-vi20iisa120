# hangman display:

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]
# code here:

import random
hang_list = ["Turkey, Chicken, Tango, Zulu, Valentine, Sam, Idiot, School, Job, Cookie, Family, Dog, Cat, Grave, Zero, One, Two, Tree"]

def get_word(word):
    word - random.choice(hang_list)
    return word.upper()

def play (word):
    word_completion = '_' *]en(hang_list)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 12
    print("Lets play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print(\n)
    while guess and tries = 0:
        guess = input("Please guess a letter or a word:").upper()
         If len(guess) == 1 and guess.isalpha():
        if guess in guess_letters:
            print("You already guessed the letter"), guess)
        elif guess not in letter:
            print("is not in the word.")
            tries == 1
            guess_letters.append(guess)
        else:
            print ("Good job", guess, "is in the word!")
            guess_letters.append (guess)
            word_as_list = list(word_completion)
            word_completion = "".join(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            1
    elif len(guess) == len(word) and guess.isalpha()

    else:
        print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print(\n)



