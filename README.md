# programe-that-randomly-guess-the-number-from-1-to-10

The code imports the random module, which provides functions for generating random numbers. This module allows us to generate a random number between 1 and 10 using the random.randint() function.

The code uses the random.randint(1, 10) function to generate a random number and assigns it to the variable guess_number. This number represents the secret number that the user needs to guess.

The code then prompts the user to guess the secret number by displaying the message "I have chosen a number between 1 and 10. Try to guess it." using the print() function.

The code enters a while loop that continues indefinitely until the user guesses the correct number. Within the loop, the user is prompted to enter their guess using the input() function. The entered guess is converted to an integer using int() and stored in the variable guess.

Inside the loop, the code compares the user's guess (guess) with the secret number (guess_number). If the guess is correct, the code displays the message "Congratulations! You guessed the secret number." using the print() function and breaks out of the loop using the break statement. If the guess is incorrect, the code displays the message "That is incorrect. Guess again." using the print() function and the loop continues.
