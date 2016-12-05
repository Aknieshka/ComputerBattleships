from Board import Board
from Player import Player
from Ship import Ship

def getCurrentPlayer(round):
    return player1 if round % 6 < 3 else player2

def getCurrentPlayerV2(round):
    return player1 if round % 2 < 1 else player2

def getOtherPlayer():
    return player1 if currentPlayer == player2 else player2

def PrintBoards():
    size = board1.boardSize
    print("     p1 board                    p2 board")
    for y in range(size):
        row = []
        for board in [board1, board2]:
            for x in range(size):
                if board.GetIdAtCoord(x,y) is None:
                    row.append("- ")
                else:
                    row.append(str(board.GetIdAtCoord(x, y))+" ")
            row.append("      ")
        print("".join(row))
    print("")

if __name__ == "__main__":

    board1 = Board()
    board2 = Board()
    player1 = Player(board2, 1)
    player2 = Player(board1, 2)
    round = 0
    PrintBoards()

    while True:
        currentPlayer = getCurrentPlayerV2(round)
        otherPlayer = getOtherPlayer()
        currentPlayer.PlayersMove()
        PrintBoards()
        if currentPlayer.won:
            print("PLAYER", currentPlayer.id, "WON")
            break
        round += 1

#    for round in range(20):
#        currentPlayer = getCurrentPlayer(round)
#        otherPlayer = getOtherPlayer()
#        currentPlayer.PlayersMove()
#        PrintBoards()




