import random

class Player:

    def __init__(self, board, id):
        print("Player created")
        self.id = id
        self.won = False
        self.opponentBoard = board
        self.lastHits = []
        self.possibleShots = []
        self.move = 0

    def PlayersMove(self):
        if self.move == 0:
            self.RandomShoot()
        else:
            self.ShootAfterHit()

    def RandomShoot(self):
        shootCoordinates = random.choice(self.opponentBoard.GetAvailableCoordinates())
        print("PLAYER", self.id, ":RANDOM SHOOT ", shootCoordinates)
        result = self.opponentBoard.Shot(shootCoordinates)

        if result == 1:
            self.opponentBoard.SetIdAtCoord(shootCoordinates[0], shootCoordinates[1], None)
            self.move = 1
            self.ExtendLastHits(shootCoordinates)
            self.ShootAfterHit()

    def ShootAfterHit(self):
        if not self.possibleShots:
            self.possibleShots = self.CreatePossiblities()

        shootCoordinates = random.choice(self.possibleShots)
        print("PLAYER", self.id, ":SHOOT AFTER HIT ", shootCoordinates)
        result = self.opponentBoard.Shot(shootCoordinates)
        if result == 0:
            self.possibleShots.remove(shootCoordinates)
        if result == 1:
            self.ShipHit(shootCoordinates)
        if result == 2:
            self.ShipSank()
        if result != 0:
            self.opponentBoard.SetIdAtCoord(shootCoordinates[0], shootCoordinates[1], None)

    def ShipHit(self, shootCoordinates):
        self.move = 2
        self.possibleShots = []
        self.ExtendLastHits(shootCoordinates)
        self.ShootAfterHit()

    def ShipSank(self):
        self.move = 0
        self.lastHits = []
        self.possibleShots = []
        if len(self.opponentBoard.leftShips) == 0:
            self.won = True
        else:
            self.RandomShoot()

    def CreatePossiblities(self):
        tmpPossibilities = []
        tmpList = []
        x0 = self.lastHits[0][0]
        y0 = self.lastHits[0][1]
        if(len(self.lastHits) == 1):
            tmpPossibilities.append([x0 - 1, y0])
            tmpPossibilities.append([x0 + 1, y0])
            tmpPossibilities.append([x0, y0 - 1])
            tmpPossibilities.append([x0, y0 + 1])
        else:
            if(x0 == self.lastHits[1][0]):
                for val in self.lastHits:
                    tmpList.append(val[1])
                tmpPossibilities.append([x0, min(tmpList)- 1])
                tmpPossibilities.append([x0, max(tmpList) +1])
            else:
                for val in self.lastHits:
                    tmpList.append(val[0])
                tmpPossibilities.append([min(tmpList) - 1, y0])
                tmpPossibilities.append([max(tmpList) + 1, y0])

        return self.RemoveNotPossible(tmpPossibilities)

    def RemoveNotPossible(self, tmpPossibilities):
        for item in list(tmpPossibilities):
            if (item not in self.opponentBoard.GetAvailableCoordinates()):
                tmpPossibilities.remove(item)
        return tmpPossibilities

    def ExtendLastHits(self, shootCoordinates):
        self.lastHits.append(shootCoordinates)
