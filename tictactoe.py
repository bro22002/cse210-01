"""
Tic-Tac-Toe
Author: Stephen Richard Brown
"""

board=['0','1','2','3','4','5','6','7','8','9']
empty = [1,2,3,4,5,6,7,8,9]

def main():
  player = 0
  while empty and check_win():    
    display_board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("NO WINNER!")

def display_board():
  print()
  print(board[1]+' | '+board[2]+' | '+board[3])
  print('- + - + -')
  print(board[4]+' | '+board[5]+' | '+board[6])
  print('- + - + -') 
  print(board[7]+' | '+board[8]+' | '+board[9])
  print()

def player_input(player):
  player_symbol = ['X','O']
  correct_input = True

  position = int(input("{symbol}'s turn to choose a square (1-9): ".format(playerNo = player +1, symbol = player_symbol[player])))

  if board[position] == 'X' or board[position] == 'O':
    correct_input = False
  
  if not correct_input:
    print("Position already equipped")
    player_input(player)
  else:
    empty.remove(position)
    board[position] = player_symbol[player] 
    return 1

def check_win():
  #define players symbols and winning positions
  player_symbol = ['X','O']
#   winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  winning_positions =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

  #check all winning positions for matching placements
  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if board[point] !=  first_symbol:
          won = False
          break
      if won:
        if first_symbol == player_symbol[0]:
          print('player x won')
        else:
          print('player o won')
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1

if __name__ == '__main__':
  main()