"""
Classes and functions to build a FEN out of some specified requisites
"""

from itertools import groupby
import random
import numpy as np


def pawns_on_extreme_ranks(piece, rank):
    """
    Utility function:
    check whether a pawn is on the first or eight rank (such event is not possible in chess)
    """
    return bool(piece in ['P', 'p'] and rank in [0, 7])


def rle(array):
    """
    Utility function:
    Compute the lengths and values of runs of equal values in an array
    """
    return [(k, sum(1 for _ in g)) for k, g in groupby(array)]


def fen_for_single_rank(lst):
    """
    Utility function:
    Returns the FEN for a single rank
    """
    lst = [str(e[1]) if e[0] == ' ' else e[0] for e in lst]
    return ''.join(lst)


class ChessBoard:
    """
    Class that creates a chessboard and its Forsyth-Edwards Notation
    (https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)

    Parameters
    ----------
    randomized : bool, default True
        Are the number and types of pieces on the board randomized?
    extra_populated : bool, default False
        If False, the maximum amount of each piece will be the same as the starting position:
        8 pawns, 2 knights/bishops/rooks, 1 queen
        If True, we could have a maximum of 8 pieces per piece type:
        8 pawns/knights/bishops/rooks/queens
    equal_material: bool, default False
        If True, the piece types will be balanced for the two players
    pieces_dict: dict, optional
        If specified, the chessboard will be generated with those amount of pieces.
        Accepted keywords: `n_pieces_<color>` or `<color>_<piece>`
        e.g. `n_pieces_white`, `white_pawns`, `black_rooks`, ...

    Returns
    -------
    ChessBoard
        Object with `self.board` as the actual board, and `self.fen` as the actual FEN
    """
    def __init__(self, randomized=True, extra_populated=False, equal_material=False, pieces_dict=None):
        if pieces_dict is not None:
            randomized = False
        self.randomized = randomized
        self.extra_populated = extra_populated
        self.equal_material = equal_material
        if pieces_dict is None:
            pieces_dict = {}
        self.pieces_dict = pieces_dict
        # initialize board
        self.board = np.full((8, 8), ' ')
        self.fen = ''
        self.pieces_list = ['P', 'N', 'B', 'R', 'Q']


    def pieces_random_amount(self):
        """
        Define the number of pieces on the board
        """
        if self.randomized:
            if self.extra_populated:
                if self.equal_material:
                    self.pieces_dict['n_pieces_white'] = self.pieces_dict['n_pieces_black'] = random.randint(0, 31)
                else:
                    self.pieces_dict['n_pieces_white'] = random.randint(0, 31)
                    self.pieces_dict['n_pieces_black'] = random.randint(0, 31)
            else:
                if self.equal_material:
                    self.pieces_dict['white_pawns'] = self.pieces_dict['black_pawns'] = random.randint(0, 8)
                    self.pieces_dict['white_knights'] = self.pieces_dict['black_knights'] = random.randint(0, 2)
                    self.pieces_dict['white_bishops'] = self.pieces_dict['black_bishops'] = random.randint(0, 2)
                    self.pieces_dict['white_rooks'] = self.pieces_dict['black_rooks'] = random.randint(0, 2)
                    self.pieces_dict['white_queens'] = self.pieces_dict['black_queens'] = random.randint(0, 1)
                else:
                    self.pieces_dict['white_pawns'] = random.randint(0, 8)
                    self.pieces_dict['white_knights'] = random.randint(0, 2)
                    self.pieces_dict['white_bishops'] = random.randint(0, 2)
                    self.pieces_dict['white_rooks'] = random.randint(0, 2)
                    self.pieces_dict['white_queens'] = random.randint(0, 1)
                    self.pieces_dict['black_pawns'] = random.randint(0, 8)
                    self.pieces_dict['black_knights'] = random.randint(0, 2)
                    self.pieces_dict['black_bishops'] = random.randint(0, 2)
                    self.pieces_dict['black_rooks'] = random.randint(0, 2)
                    self.pieces_dict['black_queens'] = random.randint(0, 1)
        else:
            pass


    def place_kings(self):
        """
        Place the two kings on the board making sure that they are not adjacent
        """
        while True:
            rank_white = random.randint(0, 7)
            file_white = random.randint(0, 7)
            rank_black = random.randint(0, 7)
            file_black = random.randint(0, 7)
            diff_list = [abs(rank_white - rank_black), abs(file_white - file_black)]
            if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):
                self.board[rank_white, file_white] = 'K'
                self.board[rank_black, file_black] = 'k'
                break


    def populate_board_randomized(self):
        """
        Place pieces on the board making sure that they are not on the same tile
        This function is used when `self.randomized` and `self.extra_populated` are both True
        """
        # iterate for white (first) and black (after) player
        # TODO: quando c'è sia extra_populated che equal_material True, i pezzi devono essere gli stessi,
        # TODO: non basta che siano uguali il numero totale dei pezzi
        for color in ['white', 'black']:
            if color == 'white':
                n_pieces = self.pieces_dict.get('n_pieces_white', 0)
                pieces_list = self.pieces_list
            else:
                n_pieces = self.pieces_dict.get('n_pieces_black', 0)
                pieces_list = [p.lower() for p in self.pieces_list]

            # insert pieces until there are no more left
            while n_pieces > 0:
                rank = random.randint(0, 7)
                file = random.randint(0, 7)
                piece = random.choice(pieces_list)
                # check if square is empty and we have not a pawn on extreme ranks
                if self.board[rank, file] == ' ' and not pawns_on_extreme_ranks(piece, rank):
                    self.board[rank, file] = piece
                    n_pieces -= 1


    def populate_board_specific(self):
        """
        Place pieces on the board making sure that they are not on the same tile
        This function is used when at least one between `self.randomized` and `self.extra_populated` is False
        """
        # generate initial set of pieces
        pieces_list = self.pieces_list + [p.lower() for p in self.pieces_list]
        pieces_amounts = [
            self.pieces_dict.get('white_pawns', 0),
            self.pieces_dict.get('white_knights', 0),
            self.pieces_dict.get('white_bishops', 0),
            self.pieces_dict.get('white_rooks', 0),
            self.pieces_dict.get('white_queens', 0),
            self.pieces_dict.get('black_pawns', 0),
            self.pieces_dict.get('black_knights', 0),
            self.pieces_dict.get('black_bishops', 0),
            self.pieces_dict.get('black_rooks', 0),
            self.pieces_dict.get('black_queens', 0)
            ]
        pieces = np.repeat(pieces_list, pieces_amounts).tolist()

        # insert pieces until there are no more left
        while len(pieces) > 0:
            rank = random.randint(0, 7)
            file = random.randint(0, 7)
            piece = pieces[0]
            # check if square is empty and we have not a pawn on extreme ranks
            if self.board[rank, file] == ' ' and not pawns_on_extreme_ranks(piece, rank):
                self.board[rank, file] = piece
                pieces.pop(0)


    def populate_board(self):
        """
        Chooses between populating the board randomly or specifically
        """
        # place kings first
        self.place_kings()

        # establish the amount of pieces to be put on the board (if randomized has been chosen)
        if self.randomized:
            self.pieces_random_amount()

        # procedure for random or specific FEN
        if self.randomized and self.extra_populated and self.equal_material:
            self.populate_board_randomized()
        else:
            self.populate_board_specific()


    def generate_fen(self):
        """
        Generate, as string, the FEN out of a given input board
        """
        # generate list of list of tuples
        fen = [rle(self.board[i]) for i in range(8)]
        # generate list of FEN's for each rank
        fen = [fen_for_single_rank(l) for l in fen]
        # unite the single-rank FEN's
        fen = '/'.join(fen) + ' w - - 0 1'
        self.fen = fen
