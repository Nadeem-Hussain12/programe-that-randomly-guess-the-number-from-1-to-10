#!/usr/bin/env python
# coding: utf-8

# # programe that guess the number between 1 to 10 

# In[7]:


import random
guess_number = random.randint(1, 10)
print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Your guess: "))

    if guess == guess_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("That is incorrect. Guess again.")


# In[ ]:




