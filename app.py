from flask import Flask, render_template, request
from chess_exercises.fen import ChessBoard


app = Flask(__name__)


@app.route("/homepage", methods=['GET'])
def home():
    """
    Homepage
    """
    return render_template("homepage.html")


@app.route("/exercises", methods=['GET', 'POST'])
def exercises():
    """
    Page with the exercises that will return the FEN and the chessboard image
    """
    if request.method == 'POST':

        # get parameters
        data = request.form
        randomized = bool(data.get('randomized', True))
        extra_populated = bool(data.get('extra_populated', False))
        equal_material = bool(data.get('equal_material', False))
        pieces_dict = {k: int(v) for k, v in data.items() if k.startswith(('white', 'black')) and v != '0'}
        # by default, the form always returns the entries of the amount of pieces
        pieces_dict = None if len(pieces_dict) == 0 else pieces_dict

        # initialize board
        board = ChessBoard(
            randomized=randomized,
            extra_populated=extra_populated,
            equal_material=equal_material,
            pieces_dict=pieces_dict
        )

        # generate board
        board.populate_board()
        board.generate_fen()

        return render_template("exercises.html", fen=board.fen, board=board.board)

    return render_template("exercises.html")
