# 3.3 Added the choice of how many letters to play.

import random
from words_58k import word_list

print("Let's play HANGMAN!")
game_level = input("(H)ard, (M)edium, (E)asy, or (R)andom level? ").upper()
hard_words = [word for word in word_list if len(word) >= 11] # Game Level Hard = 11 or more Letters
med_words = [word for word in word_list if len(word) >= 6 and len(word) <= 10]  # Game Level Medim = 6 to 10 Letters
easy_words = [word for word in word_list if len(word) <= 6] # Game Level Easy = < 6 Letters

if game_level == "H":
    def get_word():
     word = random.choice(hard_words) # choose random hard word
     return word.upper()
elif game_level == "M":
    def get_word():
     word = random.choice(med_words) # choose random medium word
     return word.upper()
elif game_level == "E":
   def get_word():
    word = random.choice(easy_words) # choose random easy word
    return word.upper()


else:
    def get_word():
     word = random.choice(word_list)
     return word.upper()

# Game Play starts
def play(word):
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        print("There are", len(word), "letters in the word.\n You've guessed these letters so far: ", guessed_letters, '\n')
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.", guess)
            elif guess not in word:
                print(guess, "Not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job!", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess.')
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you've guessed the word. You Win!")
    else:
        print("HANGMAN! The word was: " + word)

def display_hangman(tries):
    stages = [ 
                """
                     ________
                    |       |
                    |       O
                    |      \|/
                    |       | 
                    |     _/ \_
                    |
                   ----   
                """,

                """
                     ________
                    |       |
                    |       O
                    |      \|
                    |       | 
                    |     _/ \_
                    |
                   ---- 
                """,

                """
                     ________
                    |       |
                    |       O
                    |       |
                    |       | 
                    |     _/ \_
                    |
                   ----    
                """,

                """
                     ________
                    |       |
                    |       O
                    |       |
                    |       | 
                    |     _/
                    |
                   ----    
                """,

                """
                     ________
                    |       |
                    |       O
                    |       |
                    |       | 
                    |
                    |
                   ----      
                """,

                """
                     ________
                    |       |
                    |       O
                    |
                    |
                    |
                    |
                   ----  
                """, 
                
                """
                     ________
                    |       |
                    |
                    |
                    |
                    |
            Sombody | Get a Rope
                   ----   
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Do you want to play again? (Y/N) ").upper() == 'Y':
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()