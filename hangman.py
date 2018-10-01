# hangman.py 

def main():
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        display_letters(secret_word, correct_guesses)
        guess = get_guess()
        
        if len(wrong_guesses) == 0: 
         bored0 = '''        
                          _______________
                          |             |            
                                        |
                                        |
                                        |
                                        |
                                        |
                                        |
                                        | 
                                        |
                                        |
                             |====================|  ''' 

        if len(wrong_guesses) == 1:
          bored1 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                                      |
                                      |
                                      |
                                      |
                                      | 
                                      |
                                      |
                          |====================|  '''
          print(bored1)

        if len(wrong_guesses) == 2:
          bored2 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                        []            |
                        []            |
                        []            |
                                      |
                                      | 
                                      |
                          |====================|  '''
          print(bored2)

        if len(wrong_guesses) == 3:
          bored3 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                        [] \          |
                        []  \         |
                        []   O        |
                                      |
                                      | 
                                      |
                                      |
                          |====================|  '''
          print(bored3)


        if len(wrong_guesses) == 4:
          bored4 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                     /  []  \         |
                    O   []   O        |
                                      |
                                      |
                                      |
                                      |
                          |====================|   '''
          print(bored4)

        if len(wrong_guesses) == 5:
          bored5 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                    /   []  \         |
                    O   []   O        |
                        |             |
                        |             | 
                      ==|             |
                                      |
                          |====================|  '''
          print(bored5)

        if len(wrong_guesses) == 6:
          bored6 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                     /  []  \         |
                    O   []   O        |
                        ||            |
                        ||            | 
                      ==||==          |
                                      |
                          |====================|  '''
          print(bored6)

        # if guess is a word:
            # if guess is correct:
                # win
            # else:
                # lose

        # HANDLE SINGLE LETTER GUESS
        # if guess is in the word, the add it to the correct guesses
        # otherwise, add it to the incorrect guesses

    if word_solved(secret_word, correct_guesses):
        show_win_screen()
    else:
        show_lose_screen()


def get_secret_word():
    """Will return a single word from a list of words.
    Returns:
        Single word from a list
    """
    pass


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.
    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses
    Returns:
        bool: True if word is solved, False if word is not.
    """
    pass


def player_is_dead(wrong_guesses):
    """Determines if the player is dead (too many guesses).
    Args:
        bad_guesses (str): A string containing all of the wrong guesses
    Returns
        bool: True if dead, False otherwise
    """
    pass


def display_platform(wrong_guesses):
    """Displays (prints) hanging platform based on how many incorrect guesses.
    Args:
        wrong_guesses (str): A string containing all wrong guesses.
    """
    pass


def display_letters(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.
    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    pass


def get_guess():
    """Will take the user's guess. Ensures the input is valid.
    """
    pass


def show_win_screen():
    """Will display ASCII art for a win screen"""
    pass


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    pass


if __name__ == "__main__":
    main()
