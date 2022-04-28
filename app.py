import json
from flask import Flask, render_template, request, Response
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
        fen = 'EUREKA!'
        # randomized = request.data.get('randomized')
        # extra_populated = request.data.get('extra_populated')
        return render_template("exercises.html", fen=fen)

    return render_template("exercises.html")

    # data = None
    # if request.content_type == "application/json":
    #     data = json.loads(request.data)
    # else:
    #     return Response(response="This predictor only supports JSON data.", status=415, mimetype="text/plain")

    # # # Do the prediction
    # # predictions = ScoringService(data).predict()

    # # Convert from json to string
    # result = json.dumps({'bella': 'ciao'})

    # return Response(response=result, status=200, mimetype="application/json")
