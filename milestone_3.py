while True:
    guess = input("Guess a letter: ")  # Step 2

    if guess.isalpha() and len(guess) == 1:  # Step 3
        break  # Step 4
    else:
        print("Step 5: Invalid letter. Please, enter a single alphabetical character.")  # Step 5


# %%  task 2 
if guess in word:  # Step 1
            print(f"Good guess! {guess} is in the word.")  # Step 2
            break
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")  # Step 3:
# %% task 3 

def check_guess(guess):
    # Step 2
    guess = guess.lower()
    # Step 3
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        
        if guess.isalpha() and len(guess) == 1:
            
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4
ask_for_input()


# %%
