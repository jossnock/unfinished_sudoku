sudoku_board = [['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','',''],
                ['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','',''],
                ['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']]

def sudoku_player(sudoku_board):
    def sudoku_print(sudoku_board):
        pass
    sudoku_print(sudoku_board)
    current_position = input('Position a digit')
    #first part corresponds to column, second for mark
    current_position_column = 
    current_position_row = 
    current_digit = input('Which number?')
    sudoku_board[current_position_row][current_position_column] = current_digit
    

"""
Todo:
 - make UI (maybe add row/column numbers/letters)
 - implement number placing
 - make notes

 - use % to find which coords are in the boxes
"""