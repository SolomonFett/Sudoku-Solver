from scraper import getBoard

# this method is used to print the board both
# before and after solving the sudoku
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# this method is used to find the nearest valid empty cell
def findEmptyCell(board):
    # loop through every row and column to find the
    # nearest empty cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# this method is used to check if the constraints are met
def constraints(board, val, pos):
    # Check that the valber being inserted does not 
    # appear in the row already (check that we did
    # not just insert a valber into the same location)
    for i in range(len(board[0])):
        if board[pos[0]][i] == val and pos[1] != i:
            return False

    # Check that the valber being inserted does not 
    # appear in the column already (check that we did
    # not just insert a valber into the same location)
    for i in range(len(board)):
        if board[i][pos[1]] == val and pos[0] != i:
            return False

    # use floor division to figure out in which of the
    # nine large boxes (3 cells by 3 cells) the cell 
    # belongs to 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Using the above, Check that the valber being 
    # inserted does not appear in the 3 by 3 box that
    # the given cell belongs to
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == val and (i,j) != pos:
                return False
    # if all contraints are met, then we are allowed
    # to instert the valber in the current cell
    return True

# this method uses the backtracking algorithm to
# solve the Soduku board
def solver(board):
    # retrieve a valid empty cell
    # since our algorithm proceeds from left to
    # right, we will retrieve the next available 
    # cell to the right (or below) our current cell
    find = findEmptyCell(board)

    # base case: if a valide empty cell is not 
    # found, that means we have reached the end of
    # the board (far bottom right corner)
    if not find:
        return True
    else:
        # else set vars from found empty cell
        row, col = find

    #  we use the backtracking algorithm to be able
    #  to recursively find a solion to the sudoku
    #  board
    for i in range(1,10):
        # check if constraints are met
        if constraints(board, i, (row, col)):
            board[row][col] = i

            if solver(board):
                return True
            # backtracking step: if the value we've
            # does not solve the sudoku puzzle,
            # reset that value, backtrack and find
            # an alternative solution
            board[row][col] = 0

    return False

def main():
    # get an unsolved sudoku board by scraping (https://www.sudokuweb.org/)
    board = getBoard()
    print("=====================")
    print("Scraped Sudoku Board: ")
    print("=====================")

    # print the board to be solved
    printBoard(board)

    # solve the sudoku board
    solver(board)

    # print the solution
    print()
    print("=====================")
    print("Solution: ")
    print("=====================")
    printBoard(board)
    

if __name__ == '__main__':
    main()
