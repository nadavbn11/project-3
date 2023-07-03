import time
import random
from Score import add_score
from Utils import Screen_cleaner

def memoryGame(difficulty):
    print("*****  memory game  ******")
    error = 0
    list=[None]*difficulty
    random_list = []
    selected_list = []
    for num in list:
        random_list.append(random.randint(1, 101))
    print("remember the number")
    for num in random_list:
        print (num , end="  ")
    time.sleep(0.7)
    Screen_cleaner()
    i=0
    print(f"select {difficulty} number between 1-101")
    while (i<difficulty):
        try:
            selected_list.append(int(input()))
            i+=1
        except:
            print("wrong value try again")
            error+=1
    sorted_randon=sorted(random_list)
    sorted_selected=sorted(selected_list)
    if (sorted_randon==sorted_selected):
        print("********** you win ********")
        add_score(difficulty)
    else:
        print("yours choose are wrong")
    return error