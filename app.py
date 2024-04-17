from evaluation_function import Nim as EvalFuncNim
from fail_hard import Nim as FailHardMinimaxNim
from fail_soft import Nim as FailSoftMinimaxNim
from flask import Flask, redirect, render_template, request, session, url_for
from minimax import Nim as MinimaxNim

app = Flask(__name__)
app.secret_key = "your_secret_key"

nim_implementations = {
    "eval_func": EvalFuncNim,
    "fail_hard": FailHardMinimaxNim,
    "fail_soft": FailSoftMinimaxNim,
    "minimax": MinimaxNim,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    nim_type = request.form["nim_type"]
    # Nim = nim_implementations[nim_type]
    session["nim_type"] = nim_type
    session["piles"] = [7, 5, 3]  # [random.randint(1, 5) for _ in range(3)]
    session["moves"] = []

    return redirect(url_for("game"))


@app.route("/game")
def game():
    return render_template(
        "game.html",
        piles=session["piles"],
        moves=session["moves"],
        nim_type=session["nim_type"],
    )


@app.route("/move", methods=["POST"])
def move():
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
