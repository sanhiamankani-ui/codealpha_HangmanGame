import random
#list of words
words=["python","programming","codealpha","developer","website"]

#select a random word
game=random.choice(words)
#Display underscore for each letter
display= ["_"]*len(game)

#maximum wrong attempts
attempt=6

while attempt > 0:
    print(" ".join(display))
    print("Attempts left:",attempt)
    #take letter from user
    guess= input("Guess a letter: ").lower()

    if len(guess)!=1:
        print("Enter one letter")
        continue
    #check if the guessed letter is in the word
    if guess in game:
        print("Correct Guess")

        #Reveal the correct letter
        for i in range(len(game)):
            if game[i]==guess:
                display[i]=guess
    else:
        print("Wrong Guess")
        attempt=attempt-1

    #check if the player has guessed the whole word
    if "_" not in display:
        print("You win")
        break
    #Game over if all attempt used
    if attempt==0:
        print("Game Over")
        print("The word is:", game)