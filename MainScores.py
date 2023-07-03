from flask import Flask
from Score import POINTS_OF_WINNING
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

# lession 5

from waitress import serve
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    name_file = open(SCORES_FILE_NAME, 'r')
    score = int(name_file.read())
    name_file.close()
    error="could not open file"
    try:
        return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score" style="color:blue">{format(score)}</div></h1></body></html>'
    except:
       return f'<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{error}</div></h1></body></html>'

if __name__ == "__main__":
    serve(app, host="192.168.3.5", port=3000)

    # return '<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{}</div></h1></body></html>'.format(SCORE)