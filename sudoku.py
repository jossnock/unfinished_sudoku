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
    while unsolved_positions > 0: #while it's unsolved
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
        def digit_placer(position, digit):
            digit_placed = False
            while digit_placed == False:
                current_position = algebraic_notation_converter(input('Position a digit\n'))
                sudoku_board[current_position[1]][current_position[0]] = 'X' #shows position

                
                sudoku_print(sudoku_board)


        sudoku_board[current_position[1]][current_position[0]] = current_digit
        unsolved_positions += 1
        
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