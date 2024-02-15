class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

        for index, line in enumerate(self.board):
            row_list = []

            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = "|".join(str(item) for item in part)
                row_list.extend(row_square)

                # check if the current segment 'square_no' is not the last one
                if square_no != 3:
                    # append "║" at the end of row_list
                    row_list.append("║")

            # create string representation of the row with spaces between each el
            row = f'║ {" ".join(row_list)} ║\n'

            # replace rows '0' with an ' ':
            row_empty = row.replace("0", " ")

            # creating the full ASCII art representation of the sudoku art
            # add the modified row_empty to the board_string
            board_string += row_empty

            # check if the current index is less than 8: the last row of the sudoku
            if index < 8:
                # verifying if the row is the last row inside a 3x3 square
                if index % 3 == 2:
                    # create a visually appealing border if the current row
                    # is the last row of a 3x3 square
                    board_string += (
                        f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                    )

                # if the inner condition is 'False' meaning the current row is not
                # the last row of a 3x3 square
                else:
                    board_string += middle_lines
            # handling the last row when the outer if condition is false
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        """A function that finds the empty cells in the sudoku board."""
        for row, contents in enumerate(self.board):
            try:
                # attempting to find the index of the first occurence of 0
                col = contents.index(0)
                return row, col
            except ValueError:
                # if the value 0 is not present in the current row
                # except block should pass and continue to the next row
                pass

        # if no empty cells are found within the loop
        # returning None indicates that the board is filled
        return None

    def valid_in_row(self, row, num):
        """
        A function that checks if a given number can be inserted into a
        specifie row of the sudoku board.
        """

        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        A function that checks if a number can be inserted in a specified
        column of the sudoku board by checking if the number is not already
        present in that column for any row.
        """
        # the expression generates a list of boolean values representing
        # wheter the condition is True or False for each element in the specified
        # column across all rows
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """A function that checks if a number can be inserted in the 3x3 square"""
        # calculate the starting row index for the 3x3 block in the board grid
        row_start = (row // 3) * 3

        # calculate the starting column index for the 3x3 block in the board grid
        col_start = (col // 3) * 3

        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # check if the current cell in self.board is equal to num
                if self.board[row_no][col_no] == num:
                    return False  # indicates that the number cannot be inserted

        # If the number is not present, it can be inserted into the square
        # without violating the rules of the sudoku
        return True

    def is_valid(self, empty, num):
        """
        A function that check if a given number is a valid choice for an
        empty cell in the sudoku board by validating its compatibillity with
        the row.

        :params:
        :empty: a tuple representing the row and column indices of an empty cell
        :num: the number to be checked

        """
        # unpacking tuple
        row, col = empty

        # check if the number is valid for insertion in the specified row
        valid_in_row = self.valid_in_row(row, num)

        # check if the number is valid for insertion in the specified column
        valid_in_col = self.valid_in_col(col, num)

        # check if the number is valid for insertion in the 3x3 square
        valid_in_square = self.valid_in_square(row, col, num)

        # verify that all the function calls return True
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        A function that attempts to solve the sudoku by modifying the existing
        sudoku board rather than creating a new one.
        """
        # check if there are any empty cells left in the sudoku board
        # ':=' walrus operator to combine the assignment and the conditional check
        if (next_empty := self.find_empty_cell()) is None:
            # if there are no empty cells, return True - puzzle is solved!
            return True
        else:
            # in case of empty cells left
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    # if the guess is valid, the method updates the sudoku board
                    # with the guess by assigning 'guess' to the cell specified
                    # by 'next_empty'
                    row, col = next_empty

                    # access the cell at the given row and column in the sudoku board
                    # assign the value of guess
                    self.board[row][col] = guess

                    # to solve the rest of the sudoku, using recursive method
                    if self.solver():
                        return True

                    # if self.solver() call returns True, 'guess' led to an unsolvable sudoku
                    # Undo the guess by setting the cell value back to 0
                    self.board[row][col] = 0

        # case scenario, method returns False when none of the guesses leads to a solution
        return False


# Function to print and solve the sudoku board:
def solve_sudoku(board):
    gameboard = Board(board)
    print(f"\nPuzzle to solve:\n{gameboard}")

    if gameboard.solver():
        print("\nSolved puzzle: ")
        print(gameboard)

    else:
        print("\nThe provided puzzle is unsolvable.")

    return gameboard


def main():
    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5],
    ]

    # solved_sudoku = solve_sudoku(puzzle)
    # print(solved_sudoku)
    solve_sudoku(puzzle)


if __name__ == "__main__":
    main()
