from flask import Flask, session, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    """Show the board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    times_played = session.get("times_played", 0)

    return render_template("home_page.html", board=board, highscore=highscore, times_played=times_played)

@app.route("/check-dict")
def check_dict():
    """Check if word is in dictionary."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update times_played, update high score if appropriate."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    times_played = session.get("times_played", 0)

    session['times_played'] = times_played + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord = score > highscore)
     