# A program give a 2D list minesweeper game board followed by a 2D list showing the number of mines adjacent each free space on the board. 

# This function calculates the number of free spaces adjacent each mine on the board through nested for loops and if statements.
# This inner loop iterates over the columns in the 5x5 board
# This outer loop iterates over the rows in the 5x5 board

def minesweep(board):
  for row in range(5):
        for col in range(5):
            # This if statement check if each item in the list is equal to "-".
            if board[row][col] == "-":
                count = 0 
                # The count variable is set at 0, this will keep track of the number of adjacent mines for each item in the list.
                for row_mine in range(max(0, row-1), min(5, row+2)):
                    # two nested loops iterate over the surrounding items of each current item in the 2D list.
                    for col_mine in range(max(0, col-1), min(5, col+2)): # The max() and min() ensures the loop stays within the range of the board.
                        if board[row_mine][col_mine] == "#": # If an adjacent item contains a "#" the count variable is incremented by 1.
                            count += 1
                # This converts the count to a string.
                board[row][col] = str(count) 

  return board

# This is the game board the program uses. 
board = [["-", "#", "-", "-", "#"],
         ["-", "#", "-", "#", "-"],
         ["-", "-", "#", "-", "-"],
         ["-", "#", "#", "-", "-"],
         ["#", "-", "-", "-", "-"]]

intro = print("\nThis is the game layout.\n")

# This for loop prints the game loop.
for row in board:
    for num in row:
      print(num, end= " ")
    print()

print('''\n
This show the number of mines adjacent each empty space.\n  ''')

# This for loop uses the function to print the game board showing how many mines "#" are adjacent each "-" on the board.
for row in minesweep(board):
    for num in row:
      print(num, end= " ")
    print()