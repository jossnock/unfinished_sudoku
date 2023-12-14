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
            #checks if its a valid input
            ##return position


        #asking for position and digit:
        digit_position_confirmed = False
        while digit_position_confirmed == False:
            current_position = algebraic_notation_converter(input("Position a digit: "))
            sudoku_board[current_position[1]][current_position[0]] = 'X' #marks position to confirm that the player got the correct position
            sudoku_print(sudoku_board)
            
            confirmation = input("Is this the correct position? (y/n)\n").lower()
            if confirmation == 'y':
                digit_position_confirmed = True
            elif confirmation == 'n':
                continue
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        

        digit_value_valid = False
        while digit_value_valid == False:
            try:
                current_digit = input('Choose a digit between 0 and 9:')
                
                if current_digit.isdigit():
                    current_digit = int(current_digit)
                    if 0 <= current_digit <= 9:
                        digit_value_valid = True
                    else:
                        print('Input is not between 0 and 9.')
                else:
                    print('Invalid input. Please enter a valid integer.')

            except ValueError:
                print('Invalid input. Please enter a digit between 0 and 9.')

        sudoku_board[current_position[1]][current_position[0]] = current_digit
        unsolved_positions += 1

        sudoku_print(sudoku_board)
        
    print("Congradulations! You've completed this Sudoku puzzle.")





sudoku_player(sudoku_board)

    
"""
Todo:
 - make UI (maybe add row/column numbers/letters)
 - implement number placing
 - implement notes functionality (different colour?)
 - use % to find which coords are in the boxes
"""