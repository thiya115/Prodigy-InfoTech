import random

class GuessGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.guessed_correctly = False

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.target_number:
            return "Too low! Try again."
        elif guess > self.target_number:
            return "Too high! Try again."
        else:
            self.guessed_correctly = True
            return f"Congratulations! You guessed the number in {self.attempts} attempts."

    def start_game(self):
        print("Welcome to 'Guess the Number'!")
        print("I have selected a number between 1 and 100. Try to guess it!")
        while not self.guessed_correctly:
            guess = input("Enter your guess: ")

            if not guess.isdigit():
                print("Invalid input. Please enter a valid integer.")
                continue

            guess = int(guess)
            feedback = self.make_guess(guess)
            print(feedback)

def main():
    game = GuessGame()
    game.start_game()

if __name__ == "__main__":
    main()
