from evaluation_function import Nim as EvalFuncNim
from fail_hard import Nim as FailHardMinimaxNim
from fail_soft import Nim as FailSoftMinimaxNim
from flask import Flask, redirect, render_template, request, session, url_for
from minimax import Nim as MinimaxNim

app = Flask(__name__)
app.secret_key = "shhh"

nim_implementations = {
    "eval_func": EvalFuncNim,
    "fail_hard": FailHardMinimaxNim,
    "fail_soft": FailSoftMinimaxNim,
    "minimax": MinimaxNim,
}


@app.route("/")
def index():
    """
    Renders the index page where users pick their AI opponent.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    """
    Handles the "/play" route.
    Retrieves the chosen Nim implementation type from the form data,
    initializes the game session, and redirects to the game page.

    Returns:
        Response: A redirect response to the game page.
    """
    nim_type = request.form["nim_type"]
    # Nim = nim_implementations[nim_type]
    session["nim_type"] = nim_type
    session["piles"] = [7, 5, 3]  # [random.randint(1, 5) for _ in range(3)]
    session["moves"] = []

    return redirect(url_for("game"))


@app.route("/game")
def game():
    """
    Renders the game page with the current game state,
    including piles, moves, and Nim type.

    Returns:
        str: The rendered HTML content of the game page.
    """
    return render_template(
        "game.html",
        piles=session["piles"],
        moves=session["moves"],
        nim_type=session["nim_type"],
    )


@app.route("/move", methods=["POST"])
def move():
    """
    Handles the "/move" route.
    Processes the player's move, updates the game state, and performs the AI move.
    Redirects to the game page after each move.

    Returns:
        Response: A redirect response to the game page.
    """
    pile = int(request.form["pile"])
    stones = int(request.form["stones"])
    session["piles"][pile] -= stones
    session["moves"].append(
        f"Player removes {stones} stone(s) from pile {pile + 1} => State: {session['piles']}"
    )
    if sum(session["piles"]) == 0:
        return render_template("result.html", winner="AI", moves=session["moves"])

    Nim = nim_implementations[session["nim_type"]]
    game = Nim(session["piles"])
    ai_pile, ai_stones = game.ai_move()
    session["piles"] = game.piles
    session["moves"].append(
        f"AI removes {ai_stones} stone(s) from pile {ai_pile + 1} => State: {session['piles']}"
    )
    if sum(session["piles"]) == 0:
        return render_template("result.html", winner="Player", moves=session["moves"])
    return redirect(url_for("game"))


if __name__ == "__main__":
    app.run(debug=True)
