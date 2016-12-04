from Board import Board
from Player import Player
from Ship import Ship

if __name__ == "__main__":
    print("main func")


    board1 = Board()
    player1 = Player(board1)
    #board2 = Board()
    #player2 = Player(board2)
    player1.PlayersMove()

