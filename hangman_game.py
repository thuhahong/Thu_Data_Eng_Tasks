class Hangman:


    def __init__(self):
        self.lives = 5
        self.guess = ''
        self.word = ''
        self.secret_word = ''
        self.underscores = '_'

    def choose_word(self):
        from hangman_words import word_list
        import random

        self.word = random.choice(word_list).lower()
        self.secret_word = len(self.word) * "_"
        print(self.word)

    def word_length(self):
        if self.underscores == self.guess:
            print(self.word_length)

    def play(self):
        print(f"Welcome to Hangman! The aim of the game is to guess the letters in the word. "
              f"There are {len(self.word)} letters in the word. You have 5 lives in total. Good luck!")

    def make_guess(self):
        while self.lives != 0:
            self.guess = input("Guess a letter.")
            if self.guess in self.word:
                print("Well done!")
                print(f"You have {self.lives} lives left.")
            else:
                print("Try again.")
                self.lives -= 1
                print(f"You have {self.lives} lives left.")

    def outcome(self):
        if self.secret_word == self.word:
            print("Well done, you did it!")
        else:
            print("Better luck next time!")

    def main(self):
        h = Hangman()
        h.choose_word()
        h.word_length()
        h.play()
        h.make_guess()
        h.outcome()


Hangman.main('hangman_words.py')

# need to add function for user to win game
