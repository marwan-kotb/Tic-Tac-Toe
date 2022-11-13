"""
Tic Tac Toe Player
"""
import math, copy
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return np.array([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]])


def player(board):

    # If counter of O less than X then retrun O 
    if np.count_nonzero(board == X) > np.count_nonzero(board == O):
        return O
    else:
        return X
    


def actions(board):
    
    positions = set()
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == EMPTY:
    
                positions.add((x, y))
    return positions
    


def result(board, action):

    # Making the move in a copy of the board 
    cop = copy.deepcopy(board)

    if cop[action[0]][action[1]] == EMPTY:
        try:
            cop[action[0]][action[1]] = player(board)
        except:
            raise NameError('Action is not a valid for the board')
    return cop


def winner(board):
    
    # Checking for Rows for X or O victory.
    for i in range(board.shape[0]):
        if np.all(board[i]==board[i][0])  and (X in board[i] or O in board[i]):
            return board[i][0]
    
    # Checking for col for X or O victory.
    trans_arr = board.T
    for i in range(trans_arr.shape[0]):
        if np.all(trans_arr[i] == trans_arr[i][0])  and (X in trans_arr[i] or O in trans_arr[i]):
            return trans_arr[i][0]

    # Checking for Diagonals for X or O victory.
    if np.all(board.diagonal() == board.diagonal()[0]) and (board.diagonal()[0] == X or board.diagonal()[0] == O):
        return board.diagonal()[0]
    elif np.all(np.flipud(board).diagonal(0)[::-1] == np.flipud(board).diagonal(0)[::-1][0]) and (np.flipud(board).diagonal(0)[::-1][0] == O or np.flipud(board).diagonal(0)[::-1][0] == X):
        return np.flipud(board).diagonal(0)[::-1][0]

    return None 


def terminal(board):

    # If All cells are filled or there is a winner then return True
    return (not np.isin(EMPTY, board) or winner(board) is not None)
        


def utility(board):
    
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def Max(board, alpha, beta):
    
    # Checking if its over then return utility of the winner
    if terminal(board):
        return utility(board)

    # Maximizing
    
    v = -math.inf
    for action in actions(board):

        v = max(v, Min(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
   
    return v

    

def Min(board, alpha, beta):
    
    # Checking if its over then return utility of the winner
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, Max(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v
    
       


def minimax(board):

    # Selecting best move for minimax

    if terminal(board):
        return None

    bestMove = None

    
    if player(board) == X:
        bestVal = -math.inf
        
        for action in actions(board): 
            moveVal = Min(result(board, action), -math.inf, math.inf)
            
            if (moveVal > bestVal):               
                bestMove = action
                bestVal = moveVal
    
    else:
        bestVal = math.inf
    
        for action in actions(board): 
            moveVal = Max(result(board, action), -math.inf, bestVal)
            
            if (moveVal < bestVal):               
                bestMove = action
                bestVal = moveVal
    
    return bestMove

   

        
        
    
             
        

    