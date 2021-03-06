# Problem Set 2, hangman.py
# Name: Andrii Nikitin KM-11
# Collaborators:
# Time spent:

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

wordlist=load_words()

def choose_word(wordlist):
    secret_word=random.choice(wordlist) #Randomised choise of the word from file
    return secret_word
#secret_word = "Pete"
#print(secret_word)

def is_word_guessed(secret_word, guessy):
    count=0
    lobby = ''.join(guessy)
    for i in secret_word:
        if i in lobby.lower():
            count+=1
        else:
            count+=0
    return count==len(secret_word)
#print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, ryan):
    guessy = ""
    for j in secret_word:
      if j in ryan:
        guessy += j
      else:
        guessy += "_ "
    return guessy

def get_available_letters(rayn):
    conc = ''.join(sorted(list(set(string.ascii_lowercase)-set(rayn)), key=lambda a: a.lower() ))
    return(conc)
#print(get_available_letters(letters_guessed))

def match_with_gaps(my_word, other_word):
    timing = 0
    kitty=my_word.replace(" ", "")
    if len(kitty) != len(other_word):
        return False
    for let in kitty:
        if let.isalpha():
                if kitty[timing]!=other_word[timing]:
                    return False
        elif let=="_":
                if other_word[timing] in kitty:
                    return False
        timing+=1
    return True

def show_possible_matches(my_word):
    match=[]
    for guest in wordlist:
        if match_with_gaps(my_word, guest)==True:
            match.append(guest)
    if len(match)==0:
        return("No matches found")
    else:
        mathcy=" ".join(match)
        return mathcy

def check_warning(warning, try_guess):
    if warning>0:
        warning-=1
        alert=f"You have {warning} warnings left:"
    elif warning==0:
        try_guess-=1
        alert="You have no warnings left, so you lose one guess:"
    return (warning, try_guess, alert)

def hangman(secret_word):
    #secret_word="ample"
    #print(secret_word)
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    vw = ['a','e','u','i','o']
    try_guess=6
    rayn=[]
    warning=3
    while try_guess>0 and not is_word_guessed(secret_word, rayn):
        print("-"*24)
        rule1=True
        while rule1:
            print("You have",try_guess,"guesses left.")
            print("Available letters:",get_available_letters(rayn))
            letter=str(input("Please guess a letter: ")).lower()

            if letter in set(string.ascii_lowercase) and len(letter)==1 and letter not in rayn:
                rayn.append(letter)
                if letter in secret_word:
                    print("Good guess:",get_guessed_word(secret_word, rayn))
                    rule1=False
                elif letter not in secret_word:
                    if letter in vw:
                        try_guess-=2
                    elif letter not in vw:
                        try_guess-=1
                    print("Oops! That letter is not in my word:",get_guessed_word(secret_word, rayn))
                    print("-"*24)
            elif letter not in set(string.ascii_lowercase) or letter in rayn or len(letter)!=1:
                check=check_warning(warning, try_guess)
                if letter in rayn:
                    warn="You've already guessed that letter."
                else:
                    warn="That is not a valid letter."
                try_guess=check[1]
                warning=check[0]
                print("Oops!",warn,check[2],get_guessed_word(secret_word, rayn))
                print("-"*24)
            if try_guess<=0 or is_word_guessed(secret_word, rayn)==True:
                break
        if is_word_guessed(secret_word, rayn)==True and try_guess>0:
            print("-"*24)
            print("Congratulations, you won! Your total score for this game is:", len(set(secret_word))*try_guess)
        elif try_guess<=0 and is_word_guessed(secret_word, rayn)!=True:
            print("Sorry, you ran out of guesses. The word was", secret_word)

def hangman_with_hints(secret_word):
    #secret_word="ample"
    #print(secret_word)
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    vw = ['a','e','u','i','o']
    try_guess=6
    rayn=[]
    warning=3
    while try_guess>0 and not is_word_guessed(secret_word, rayn):
        print("-"*24)
        rule1=True
        while rule1:
            print("You have",try_guess,"guesses left.")
            print("Available letters:",get_available_letters(rayn))
            letter=str(input("Please guess a letter: ")).lower()
            if letter == "*":
                print("Possible matches:", show_possible_matches(get_guessed_word(secret_word, rayn)))
                print("-"*24)
            else:
                if letter in set(string.ascii_lowercase) and len(letter)==1 and letter not in rayn:
                    rayn.append(letter)
                    if letter in secret_word:
                        print("Good guess:",get_guessed_word(secret_word, rayn))
                        rule1=False
                    elif letter not in secret_word:
                        if letter in vw:
                            try_guess-=2
                        elif letter not in vw:
                            try_guess-=1
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word, rayn))
                        print("-"*24)
                elif letter not in set(string.ascii_lowercase) or letter in rayn or len(letter)!=1:
                    check=check_warning(warning, try_guess)
                    if letter in rayn:
                        warn="You've already guessed that letter."
                    else:
                        warn="That is not a valid letter."
                    try_guess=check[1]
                    warning=check[0]
                    print("Oops!",warn,check[2],get_guessed_word(secret_word, rayn))
                    print("-"*24)
            if try_guess<=0 or is_word_guessed(secret_word, rayn)==True:
                break
        if is_word_guessed(secret_word, rayn)==True and try_guess>0:
            print("-"*24)
            print("Congratulations, you won! Your total score for this game is:", len(set(secret_word))*try_guess)
        elif try_guess<=0 and is_word_guessed(secret_word, rayn)!=True:
            print("Sorry, you ran out of guesses. The word was", secret_word)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
