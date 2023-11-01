#%%
import random
word_list = ["Strawberry", "Banana", "Apple", "Orange", "Blueberry"]
print (word_list)
word = random.choice(word_list)
print(word)
# %% task 3 
guess = input("Please enter a single letter: ")
# %% Task 4 
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
     print("Oops! That is not a valid input.")
# %%
