from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

# key names will use to store some things in the session;
# put here as constants so we're guaranteed to be consistent in our spelling of these

GAME_BOARD_SESSION = 'gameboard'

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    return render_template("/home_page.html")

@app.route("/game_started")
def play_game():
    session[GAME_BOARD_SESSION] = boggle_game.make_board()
    return render_template("/game_started.html")