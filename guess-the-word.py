import random

words = ["turtle","winter","summer","elephant","plant","book"]
secret_word = random.choice(words)
dashes = "-"*len(secret_word)
x = 0

def get_guess():
    letter = input("Guess: ")
    while True:
        if letter == letter.lower() and len(letter)==1:
            return letter
            break
        elif len(letter)>1:
            print("Your guess must have exactly one character!")
            letter = input("Guess: ")
        if not letter.islower():
            print("Your guess must be a lowercase letter!")
            letter = input("Guess: ")
        else:
            print("Your guess must be a lowercase letter!")
            letter = input("Guess: ")

def update_dashes(secret,dashes_,guess_):
    my_list = list(secret)
    dash = list(dashes_)
    for i in range(0,len(my_list)):
        if guess_ == my_list[i]:
            dash = list(dash)
            dash[i] = guess
            dash = "".join(dash)
    return dash

guesses_left = 10
while "-" in dashes and guesses_left != 0:
    print(dashes)
    print("Incorrect guess left: " + str(guesses_left))
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the secret word!")
        dashes = update_dashes(secret_word,dashes,guess)
    else:
        print("That letter is not in the secret word!")
        guesses_left = guesses_left - 1

if "-" in dashes:
    print("You lose. The word was: " + secret_word)
else:
    print("Congrats! You win! The word was: " + secret_word)