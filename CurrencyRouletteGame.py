#to chacek need to perform pip install forex-python
from forex_python.converter import CurrencyRates
import random
from datetime import date, timedelta

from Score import add_score


def CurrencyRoulette(difficulty):
    error = 0
    amount_us = random.randint(1, 100)
    guess_NIS =0
    error=0
    while guess_NIS ==0:
        try:
            guess_NIS = int(input(f"Guess how much NIS is {amount_us} USD: "))
        except:
            print("wrong value only positive number")
            guess_NIS = 0
            error+=1
    c = CurrencyRates()
    today = date.today()- timedelta(days=100)
    ils_amount = int(c.get_rate('USD', 'ILS', today))
    real_value =amount_us * ils_amount
    print("Your guess is:", guess_NIS)
    print("The real value is:",real_value )
    if (abs(guess_NIS - real_value)<=difficulty):
        print("you win")
        add_score(difficulty)
    else:
        print("sorry you lost")
    return error
