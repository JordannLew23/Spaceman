import random
from Wordlist import word_list

def choose_word():
    word = random.choice(word_list)
    return word.upper()

def play_game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Lets Play!")
    print(tries)
    print(word_completion)
    print("/n")
    while not guessed and tries > 0:
        guess = input("Please Guess a Letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess,"is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = true
                word_completion = word

        else:
            print("Not Valid Guess, Please try again.")
        print(tries)
        print(word_completion)
        print("/n")
    if guessed:
        print("Congrats, you guessed the word! YOU WIN!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def main():
    word = choose_word()
    play_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = choose_word()
        play_game(word)

if __name__ == "__main__":
    main()
