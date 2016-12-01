from Board import Board
from Player import Player
from Ship import Ship

if __name__ == "__main__":
    print("main func")
    board1 = Board()
    player1 = Player(board1)
    #player1.CreatePossibilities(2, 2, 3,2, 4, 2)
    '''
    board1 = Board()
    board1.CreateBoard()
    board1.DrawShips()
    board1.AddShipsToBoard()
    board1.CheckIfAnyShipExists()
    board1.IfHit()
    board1.ShipDestroyed()

    player1 = Player(board1)
    player1.RandomShot()
    player1.AnotherHit()
    player1.SetId()
    player1 = Player()
    player1.FirstHit(2, 2)

    ship1 = Ship()
    ship1.IsShotDown()
    ship1.CreateCoordinates(1, 1)'''
