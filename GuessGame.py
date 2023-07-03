import random
from Score import add_score

def GuessGame(difficulty):
    print("***Guess  Game *****")
    condition=True
    error = 0
    secret_number = random.randint(1,difficulty)
    your_chose=0
    while (condition):
        try:
            your_chose = int(input(f"select a number between 1 to {difficulty} \n"))
            condition=False
        except:
           error+=1
    if (secret_number == your_chose):
        print(f"you win select value was {secret_number}")
        add_score(difficulty)
    else:
        print(f"you lose you chose {your_chose} and user select {secret_number}")

    return error