from Live import *

wellcom("Nadav")

game, difficulty, BAD_RETURN_CODE = load_game()

BAD_RETURN_CODE+=playGame(game,difficulty)

print("number of error", BAD_RETURN_CODE)
