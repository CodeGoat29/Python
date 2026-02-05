import random

class NumberGuessingGame:
    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.max_attempts = 7
        self.game_over = False
    
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("🎯 Welcome to the Number Guessing Game! 🎯")
        print("=" * 40)
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}")
        print(f"You have {self.max_attempts} attempts to guess it!")
        print("Let's see if you can find it! 🤔\n")
    
    def get_user_guess(self):
        """Get and validate user input"""
        while True:
            try:
                guess = input(f"Enter your guess ({self.min_number}-{self.max_number}): ")
                guess = int(guess)
                
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}!")
                    
            except ValueError:
                print("Please enter a valid number!")
    
    def check_guess(self, guess):
        """Check the user's guess and provide feedback"""
        self.attempts += 1
        
        if guess == self.secret_number:
            self.game_over = True
            print(f"🎉 Congratulations! You guessed it! 🎉")
            print(f"The number was {self.secret_number}")
            print(f"You won in {self.attempts} attempts!")
            return True
        
        elif guess < self.secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
        
        remaining = self.max_attempts - self.attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}\n")
        
        return False
    
    def check_game_over(self):
        """Check if the game should end"""
        if self.attempts >= self.max_attempts and not self.game_over:
            print(f"💀 Game Over! You've used all {self.max_attempts} attempts.")
            print(f"The number was {self.secret_number}")
            self.game_over = True
            return True
        return False
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        while not self.game_over:
            guess = self.get_user_guess()
            correct = self.check_guess(guess)
            
            if correct:
                break
                
            if self.check_game_over():
                break
        
        self.ask_play_again()
    
    def ask_play_again(self):
        """Ask if player wants to play again"""
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                self.reset_game()
                self.play_game()
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing! Goodbye! 👋")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def reset_game(self):
        """Reset game for a new round"""
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.game_over = False
        print("\n" + "="*40)
        print("🔄 Starting a new game!")
        print("="*40)

# Enhanced version with difficulty levels
class AdvancedNumberGame(NumberGuessingGame):
    def __init__(self):
        super().__init__()
        self.difficulty_levels = {
            'easy': {'range': (1, 50), 'attempts': 10},
            'medium': {'range': (1, 100), 'attempts': 7},
            'hard': {'range': (1, 200), 'attempts': 5},
            'expert': {'range': (1, 500), 'attempts': 8}
        }
    
    def choose_difficulty(self):
        """Let player choose difficulty level"""
        print("Choose your difficulty level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        print("4. Expert (1-500, 8 attempts)")
        
        while True:
            try:
                choice = input("Enter your choice (1-4): ")
                difficulty_map = {
                    '1': 'easy', '2': 'medium', 
                    '3': 'hard', '4': 'expert'
                }
                
                if choice in difficulty_map:
                    selected = difficulty_map[choice]
                    settings = self.difficulty_levels[selected]
                    
                    self.min_number, self.max_number = settings['range']
                    self.max_attempts = settings['attempts']
                    self.secret_number = random.randint(self.min_number, self.max_number)
                    
                    print(f"🎮 {selected.title()} mode selected!")
                    print(f"Range: {self.min_number}-{self.max_number}, Attempts: {self.max_attempts}\n")
                    break
                else:
                    print("Please enter a number between 1 and 4!")
                    
            except ValueError:
                print("Please enter a valid choice!")
    
    def play_game(self):
        """Override to include difficulty selection"""
        print("🎯 Welcome to the Advanced Number Guessing Game! 🎯")
        print("=" * 50)
        self.choose_difficulty()
        super().play_game()

# Main execution
if __name__ == "__main__":
    print("Which version would you like to play?")
    print("1. Classic Number Guessing Game")
    print("2. Advanced Game with Difficulty Levels")
    
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            game = NumberGuessingGame()
            game.play_game()
            break
        elif choice == '2':
            game = AdvancedNumberGame()
            game.play_game()
            break
        else:
            print("Please enter 1 or 2!")
