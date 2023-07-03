from MemoryGame import memoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRoulette

def wellcom(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")

def load_game():
    game=0
    difficulty =0
    error=0
    while (game>3 or game<1):
        try:
            game = int(input("""Please choose a game to play:
                        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                        2. Guess Game - guess a number and see if you chose like the computer
                        3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"""))
        except:
            print("please insert number only")
            error+=1
    while (difficulty > 5 or difficulty < 1):
        try:
            difficulty= int(input("Please choose game difficulty from 1 to 5:\n"))
        except:
            difficulty=0
            print("please insert number only")
            error+=1;
    return (game, difficulty, error)

def playGame(game, level):
    if game == 1:
        error= memoryGame(level)
    elif game == 2:
        error = GuessGame(level)
    elif game == 3:
        error = CurrencyRoulette(level)
    return error
