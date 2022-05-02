def main():
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

    iterations = 0 # Amount of words to be inputted.
    while True: # Makes a constant loop for getting input.
        iterations = input("Amount of words to check: ") # Gets the user input for the amount of words to check.
        try: # Try getting an integer value from the given input.
            iterations = int(iterations)
        except ValueError: # If not given a valid number, then send a notice to the user, and try again.
            print("Invalid number.")
            continue

        break # If a number is parsed successfully, then continue down the program.


    for i in range(iterations): # Loops for the amount of words to check.
        while True:
            inp = input(f"Word {i + 1}: ") # Asks the user for the given word we are currently checking for.
            if " " in inp: # If the given input is not a single word, send a notice and try again.
                print("Please provide a single word...")
                continue

            break # If a single word is given, break from the loop.

        inputs.append(inp) # Add the given input to the inputs array.

    filtered = findChar(inputs, char) # Function call to retrieve all the given words that contain the original character.

    print(f"Words with '{char}': {filtered}") # Outputs the words found to the user.


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        pass