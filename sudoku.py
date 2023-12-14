sudoku_board = [[None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None]]

def sudoku_player(sudoku_board):
    def sudoku_finish_checker(sudoku_board):
        solved = False
        for i in range(len(sudoku_board)):
            if sudoku_board[i] == [None, None, None, None, None, None, None, None, None]:
                solved = False
            else:
                for j in range(len(sudoku_board[i])):
                    if sudoku_board[i][j] == None:
                        solved = False
        return solved

    while sudoku_finish_checker(sudoku_board) == False: #while it's unsolved
        def sudoku_print(sudoku_board):
            #prints the board neatly
            pass
            print(sudoku_board)
        sudoku_print(sudoku_board)

        def algebraic_notation_converter(algebraic_position): 
            #converts algebraic notation into a position on the grid e.g. a7 becomes 12
            pass
            ##return position

        #asking for position and digit:
        current_position = algebraic_notation_converter(input('Position a digit\n'))
        sudoku_board[current_position[1]][current_position[0]] = 'X' #shows position
        sudoku_print(sudoku_board)


        current_digit = input("Which digit? Or type 'x' to redo position.\n")
        while current_digit == 'x':
            ##current_position = 
            pass
    
        sudoku_board[current_position[1]][current_position[0]] = current_digit
        sudoku_print(sudoku_board)


        sudoku_finish_checker(sudoku_board)




sudoku_player(sudoku_board)

    
"""
Todo:
 - make UI (maybe add row/column numbers/letters)
 - implement number placing
 - implement notes functionality (different colour?)
 - use % to find which coords are in the boxes
"""