sudoku_board = [['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']
               ,['','','','','','','','','']]

def sudoku_player(sudoku_board):
    while sudoku_board.count('') > 0: #while there's empty spaces
        def sudoku_print(sudoku_board):
            #prints the board neatly
            pass
        sudoku_print(sudoku_board)

        def algebraic_notation_converter(algebraic_position): 
            #converts algebraic notation into coordinates on the grid e.g. a7 becomes 12
            pass

        #asking for position and digit:
        current_position = algebraic_notation_converter(input('Position a digit\n'))
        current_digit = input('Which digit?\n')

    
        sudoku_board[current_position[1]][current_position[0]] = current_digit
        sudoku_print(sudoku_board)









    
"""
Todo:
 - make UI (maybe add row/column numbers/letters)
 - implement number placing
 - make notes

 - use % to find which coords are in the boxes
"""