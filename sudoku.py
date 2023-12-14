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
    #first part corresponds to column, second for mark
    def algebraic_notation_converter(algebraic_position):
        pass
    current_position = algebraic_notation_converter(input('Position a digit'))

    current_position_column = current_position[0]
    current_position_row = current_position[1]
    current_digit = input('Which number?')
    sudoku_board[current_position_row][current_position_column] = current_digit
    


    








    
"""
Todo:
 - make UI (maybe add row/column numbers/letters)
 - implement number placing
 - make notes

 - use % to find which coords are in the boxes
"""