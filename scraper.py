import lxml.html
import requests

def getBoard():
    # make a request to the sites's url
    html = requests.get('https://www.sudokuweb.org/')
    # retrieve the document
    doc = lxml.html.fromstring(html.content)
    # find all rows of the DOM table that contain the board cells we want to retrieve
    input_board = doc.xpath('//table/tr/td/span[@class="sedy"]/text() | //td/span[@class="vloz"]/text()')

    # array to store the sudoku board after it has been scraped
    result_board = []
    # array to store each row
    row = []
    # colum index for each row
    col_index = 0
    # row index in result_board
    board_row_index = 0
    # count the values that have been scraped
    count = 0

    # loop through every cell of the board we scraped from
    # 'https://www.sudokuweb.org/'
    for val in input_board:
        # if we 
        if count == 80:
            result_board.insert(board_row_index, row)
        # if the index equals 9 that means we need to wrap around
        # the board and place the next cell in the 0th col_index
        # of the next row
        if col_index == 9:
            result_board.insert(board_row_index, row)
            board_row_index += 1
            row = []
            col_index = 0
        # Insert the cell value into the row array
        # the website stores empty cells as non-breaking spaces
        if val == '\xa0':
            row.append(0)
        else:
            row.insert(col_index, int(val))
        
        count += 1
        col_index += 1

    return result_board



