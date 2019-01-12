"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    #1. Display an intro/welcome message to the player.
    print("Hello Player!")

    #2. Store a random number as the answer/solution.
    solution = random.randint(0,10)
    game_over = False
    #3. Continuously prompt the player for a guess.
    attempts = 0
    while not game_over:

        # a. Check if user has chosen a correct data type (int). if not, prompt them to guess again
        try:
            guess = input("Make a guess ({0} - {1}): ".format(0, 10))

            if type(guess) != int:
                raise Exception
        except Exception:
            print("Please make sure the guess is of correct type (integer).")
            print("Try again")
            continue

        guess = int(guess)
        attempts += 1
        if solution < guess:
            #  b. If the guess greater than the solution, display to the player "It's lower".
            print("It's lower")
        elif solution > guess:
            #  c. If the guess is less than the solution, display to the player "It's higher".
            print("It's higher")
        else:
            # 4. Once the guess is correct, stop looping, inform the user they "Got it"
            # and show how many attempts it took them to get the correct number.
            game_over = True
            print ("Got it")
            print ("Number of Attempts until getting solution: {0}".format(attempts))

    #5. Let the player know the game is ending, or something that indicates the game is over.
    print ("Game Over! Thank you for playing.")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
