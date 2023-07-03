import os
from Utils import SCORES_FILE_NAME

POINTS_OF_WINNING=0;

def add_score(difficulty):
    global POINTS_OF_WINNING
    POINTS_OF_WINNING+=(difficulty*3)+5
    name_file = open(SCORES_FILE_NAME, 'a')
    if (os.stat(SCORES_FILE_NAME).st_size == 0):
        name_file.write(str(POINTS_OF_WINNING))
        name_file.close
    else:
        name_file.close()
        name_file = open(SCORES_FILE_NAME, 'r')
        value_file = int(name_file.read())
        name_file.close()
        new_value= POINTS_OF_WINNING+value_file
        name_file = open(SCORES_FILE_NAME,'w')
        name_file.write(str(new_value))
        name_file.close()
        print("Done")




