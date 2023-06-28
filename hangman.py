mode = input("Enter mode type (player or editor):").lower()
while mode != "editor" and mode != "player":
    mode = input("Enter mode type (player or editor):").lower()
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grapefruit', 'honeydew']
if mode == "editor":
    while True:                         
        print("Current list:",words)         #current list  
        print("1. Add")                         
        print("2. Change")
        print("3. Delete")
        print("4. chnage number of tries")
        print("5. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':                       
            word = input("Enter new word to add: ")
            words.append(word)
            print("Successfully added.")

        elif choice == '2':
            print("Current list:",words)
            change = input("Enter the word to change: ")
            if change in words:
                new_word = input("Enter the new word: ")
                index = words.index(change)
                words[index] = new_word
                print("Element changed successfully.")
            else:
                print("Word not found in the list.")

        elif choice == '3':
            print("Current list:",words)
            delete = input("Enter the word to delete: ")
            if delete in words:
                words.remove(delete)
                print("Element",
                      delete, "deleted successfully.")
            else:
                print("Word not found in the list.")

        elif choice == '4':
                    new_tries = int(input("Enter the new number of tries: "))
                    if new_tries > 0:
                        tries = new_tries
                        print("Number of tries changed successfully.")
                    else:
                        print("Invalid number of tries. Please enter a positive integer.")
        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

        print()  # Add a line break for better readability

    print("Final list:", my_list)
elif mode == "player":
    import random
    def Random_word():
        return random.choice(words)             # Returns a random word from the list

    def display_word(word, guessed_letters):    # Displays the word with underscores for unguessed letters
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

    def HANGMAN():
        word = Random_word()
        guessed_letters = []                    #empty list  
        tries = 6                               #number of tries after wrong guess to finish game 
        
        while tries > 0:
            display_word(word, guessed_letters)         # Display the current state of the word
            guess = input('Enter a letter: ').lower()   # Get a letter guess from the player (.lower is used to convert user input to lower case)
            if guess in guessed_letters:                # Check if the letter has already been guessed and prevent from over writng same input
                print('You already guessed that letter.')
                continue
            
            guessed_letters.append(guess)               # Add the guessed letter to the list
            
            if guess in word:                           # Check if the guess is correct
                print('Correct guess!')
            else:
                print('Incorrect guess!')
                tries -= 1
                print('Tries left:', tries)

           
            if all(letter in guessed_letters for letter in word): # Check if the word has been completely guessed
                print('Congratulations! You guessed the word:', word)
                break

        
        if tries == 0:                                  # If the player runs out of tries
            print('You lost! The word was:', word)

    HANGMAN()       #function called to start the game

else:
    print("Invalid mode type. Please choose 'player' or 'editor'.")
