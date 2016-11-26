from Board import Board
from random import randint

class Player:
    id = None
    #move = state, that tells if earlier player hit once or more
    #0 - missed
    #1 - player hit once, then missed -> next player turn -> again his turn
    #2 - hit twice and so on
    move = None
    #to not check possibleShots everytime
    possibleShots = []
    #player shoots to this board
    opponentBoard = None

    def __init__(self, board):
        print("Player created")
        self.opponentBoard = board

    def PlayersMove(self, *args):
        if self.move == 0:
            self.RandomShoot()
        elif self.move == 1:
            #args[0] = coorX, args[1] = coorY
            self.FirstHit(args[0], args[1])
        else:
            self.AnotherHit()

    def RandomShoot(self):
        print("Create here mechanism of random shot")

    #will work when availableCoordinates will be initiated
    def FirstHit(self, x, y):
        move = 1
        if not self.possibleShots:
            #creates possibilities for shots if list empty
            self.possibleShots = self.CreatePossibilities(x, y)

        #removes not possible shoots
        for item in list(self.possibleShots):
            if(item not in self.opponentBoard.availableCoordinates):
                self.possibleShots.remove(item)

        shootCoordinates = self.possibleShots[randint(0, len(self.possibleShots) -1)]
        result = self.opponentBoard.Shot(shootCoordinates)
        if result == 1:
            #first coordinates were x and y
            #second coordinates are shootCoordinates
            move = 2
            self.AnotherHit()
        if result == 2:
            move = 0
            self.RandomShot()

    def AnotherHit(self):
        print("Create here mechanism when there are more, than one hit")

    def SetId(self):
        print("Set player's id")

    def CreatePossibilities(self, x0, y0, *args):
        tmpPossibilities = []
        if args:
            #more than one hit
            print(args)
        else:
            #just one hit
            for i in range(0, 4):
                tmpPossibilities.append([])
            tmpPossibilities[0] = [x0 - 1, y0]
            tmpPossibilities[1] = [x0 + 1, y0]
            tmpPossibilities[2] = [x0, y0 - 1]
            tmpPossibilities[3] = [x0, y0 + 1]
            return tmpPossibilities

