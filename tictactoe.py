"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                counter += 1
            elif board[i][j] == O:
                counter -= 1
    if counter <= 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError

    temp_board = deepcopy(board)
    temp_board[action[0]][action[1]] = player(board)
    return temp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i] == [X, X, X] or board[i] == [O, O, O]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                counter += 1

    if counter == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return Max(board)[0]
    else:
        return Mini(board)[0]


def Max(board):

    moves = actions(board)
    best_score = -1
    best_move = tuple()

    if terminal(board):
        return (None, utility(board))

    for move in moves:
        if Mini(result(board, move))[1] >= best_score:
            best_move = move
            best_score = Mini(result(board, move))[1]
    return (best_move, best_score)


def Mini(board):

    moves = actions(board)
    best_score = 1
    best_move = tuple()

    if terminal(board):
        return (None, utility(board))

    for move in moves:
        if Max(result(board, move))[1] <= best_score:
            best_move = move
            best_score = Max(result(board, move))[1]
    return (best_move, best_score)
