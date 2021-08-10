# ----------Global variables----------
# assign turns
turn = 'X'

# empty board
theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}
# ------------------------------------

def main():
    # make turn global so you can switch from X to O
    global turn

    # prints board in board format
    printBoard(theBoard)

    # algorithm to run game
    for i in range(9):

        # ask for user input and make sure it does not coincide with a taken spot
        handleTurn(theBoard, turn)

        # update positions of board after turn
        printBoard(theBoard)

        # make sure to find a winner (put this before switch turn)
        findWinner(theBoard, turn)

        # declare tie
        tie(theBoard)

        # switching turns after each move
        turn = switch(turn)



'''functions'''

# prints board in board format
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '      1|2|3')
    print('-+-+-' + '      -+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6] + '      4|5|6')
    print('-+-+-' + '      -+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9] + '      7|8|9')

# handle turn
def handleTurn(board, player):
    # make sure place cannot be overwritten
    while True:
        try:
            # user input
            move = int(input(f'Turn for {player}. Where do you want to position yourself? \n'))
            if board[move] != ' ':
                print('That place has already been taken, make another move.')
            else:
                # assign the position of the board to the player X or O
                board[move] = player
                break
        except ValueError:
            print("Please enter a number between 1 and 9 corresponding to the board position")
            continue
        except KeyError:
            print('It has to be a number between 1-9 corresponding to the grid of the board.')
            continue

# switching turns after each move
def switch(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

# find a winner
def findWinner(board, player):
        # horizontal
        if (((board[1] == board[2] == board[3]) and (board[1] != ' ')) or ((board[4] == board[5] == board[6]) and (board[4] != ' ')) or ((board[7] == board[8] == board[9]) and (board[7] != ' '))):
            print(f'{player} has won the game!')
            exit()

        # vertical
        elif (((board[1] == board[4] == board[7]) and (board[1] != ' ')) or ((board[2] == board[5] == board[8]) and (board[2] != ' ')) or ((board[3] == board[6] == board[9]) and (board[3] != ' '))):
            print(f'{player} has won the game!')
            exit()

        # diagonal
        elif (((board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7])) and (board[5] != ' ')):
            print(f'{player} has won the game!')
            exit()

def tie(board):
    if (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        print("'Tis a tie.")
        exit()

'''run program'''
main()