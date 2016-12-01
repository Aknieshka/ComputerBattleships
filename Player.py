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
        shootCoordinates = self.opponentBoard.availableCoordinates[randint[0, len(self.opponentBoard.availableCoordinates)-1]]
        result = self.opponentBoard.Shot(shootCoordinates)
        if result == 1:
            self.FirstHit(shootCoordinates[0], shootCoordinates[1])
        if result == 2:
            move = 0
            self.RandomShoot()

    #will work when availableCoordinates will be initiated
    def FirstHit(self, x, y):
        move = 1
        if not self.possibleShots:
            #creates possibilities for shots if list empty
            self.possibleShots = self.CreatePossibilities(x, y)

        shootCoordinates = self.possibleShots[randint(0, len(self.possibleShots) -1)]
        result = self.opponentBoard.Shot(shootCoordinates)
        if result == 1:
            #first coordinates were x and y
            #second coordinates are shootCoordinates
            self.possibleShots = []
            move = 2
            self.AnotherHit(x, y, shootCoordinates[0], shootCoordinates[1])
        if result == 2:
            self.possibleShots = []
            move = 0
            self.RandomShoot()

    def AnotherHit(self, x0, y0, *args):
        if not self.possibleShots:
            #creates possibilities for shots if list empty
            if(len(args) < 3):
                self.possibleShots = self.CreatePossibilities(x0, y0, args[0], args[1])
            else:
                self.possibleShots = self.CreatePossibilities(x0, y0, args[0], args[1], args[2], args[3])
        shootCoordinates = self.possibleShots[randint(0, 1)]
        result = self.opponentBoard.Shot(shootCoordinates)
        if result == 1:
            #first coordinates were x and y
            #second coordinates are shootCoordinates
            #self.possibleShots = []
            move = 2
            self.AnotherHit(x0, y0, args[0], args[1], shootCoordinates[0], shootCoordinates[1])
        if result == 2:
            self.possibleShots = []
            move = 0
            self.RandomShoot()

    def SetId(self):
        print("Set player's id")

    def CreatePossibilities(self, x0, y0, *args):
        tmpPossibilities = []
        if args:
            for i in range(0, 2):
                tmpPossibilities.append([])
            # two hits
            if(len(args) == 2):
                if(x0 == args[0]):
                    tmpPossibilities[0] = [x0, min(y0, args[1]) - 1]
                    tmpPossibilities[1] = [x0, max(y0, args[1]) + 1]
                else:
                    tmpPossibilities[0] = [min(x0, args[0])-1, y0]
                    tmpPossibilities[1] = [max(x0, args[0])+1, y0]

            # three hits
            else:
                if (x0 == args[0]):
                    tmpPossibilities[0] = [x0, min(y0, args[1], args[3]) - 1]
                    tmpPossibilities[1] = [x0, max(y0, args[1], args[3]) + 1]
                else:
                    tmpPossibilities[0] = [min(x0, args[0], args[2]) - 1, y0]
                    tmpPossibilities[1] = [max(x0, args[0], args[2]) + 1, y0]
        # just one hit
        else:
            for i in range(0, 4):
                tmpPossibilities.append([])
            tmpPossibilities[0] = [x0 - 1, y0]
            tmpPossibilities[1] = [x0 + 1, y0]
            tmpPossibilities[2] = [x0, y0 - 1]
            tmpPossibilities[3] = [x0, y0 + 1]

        return self.RemoveNotPossible(tmpPossibilities)

    def RemoveNotPossible(self, tmpPossibilities):
        for item in list(tmpPossibilities):
            if (item not in self.opponentBoard.availableCoordinates):
                tmpPossibilities.remove(item)
        return tmpPossibilities
