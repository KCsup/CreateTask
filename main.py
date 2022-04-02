# General program info.
info = "This program is used to find a given character from a given list of words. At the beginning of the program, you will be prompted to enter " + \
    "a character. Make sure to only give it a single letter or character, as you will not be able to continue otherwise. Afterwards, you will be " + \
    "prompted to enter the amount of words that you want to check. Make sure to give a valid number, as you will not be able to continue otherwise. " + \
    "Lastly, you will be prompted to type in words to be checked later (it does not matter what you type in here). Once you have inputted all the words, " + \
    "you will be given the words that you typed that contain the letter originally stated.\n\n"
print(info)


# Finds a word in a given array that contains a given character.
def findChar(array, char):
    outs = [] # Array for outputs.
    for s in array: # Loops through all the words in the given array.
        if char.lower() in s.lower(): # Checks if the word in the array contains the given letter.
            outs.append(s) # If so, add this word to the outputs array.

    return outs # Return the output array.


inputs = []  # Array to store user inputs

char = ''  # Character variable to be updated later
while len(char) != 1: # While the given character is not one letter long.
    char = input("Character to find: ") # Ask the user for the character.
    if len(char) != 1: # If the character given is not one letter long.
        print("Invalid character. Must be a single character.") # Then print the error message and retry.

iterations = 0 # Amount of words to be inputted
while True:
    iterations = input("Amount of words to check: ")
    try:
        iterations = int(iterations)
    except ValueError:
        continue

    break


for i in range(iterations):
    inp = input(f"Word {i + 1}: ")
    inputs.append(inp)

filtered = findChar(inputs, char)

print(f"Words with {char}: {filtered}")
