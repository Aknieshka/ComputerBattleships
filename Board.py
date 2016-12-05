import random

import Ship


class Board:
    boardSize = 10
    shipSizes = [5, 4, 3, 3, 2]
    #unnecessary
    #numOfShips = 1

    def __init__(self):
        self.leftShips = []
        self.availableCoordinates = []
        self.idsGrid = None

        for i in range(10):
            for j in range(10):
                self.availableCoordinates.append([i, j])
        self.idsGrid = [[None for i in range(self.boardSize)] for i in range(self.boardSize)]
        self.CreateBoard()

    def CreateBoard(self):
        id = 0
        for i in range(len(self.shipSizes)):
            masts = self.shipSizes[i]
            #unnecessary loop
            ship = self.DrawShip(id, masts)
            self.AddShipToBoard(ship)
            id += 1

    def DrawShip(self, id, masts):
        direction = random.choice(["horizontal", "vertical"])
        upperLeftCoord = random.choice(self.GetPossibleUpperLeftCoord(masts, direction))
        ship = Ship.Ship(id, masts, direction, upperLeftCoord)
        return ship

    def GetPossibleUpperLeftCoord(self, masts, direction ):
        possibleUpperLeftCoords = []
        for upperLeftX in range(self.boardSize):
            for upperLeftY in range(self.boardSize):
                shipCoord = self.GetShipCoords(upperLeftX, upperLeftY, masts, direction)
                if self.CanShipBeAddedAtCoordinates(shipCoord):
                    possibleUpperLeftCoords.append([upperLeftX, upperLeftY])
        return possibleUpperLeftCoords

    def CanShipBeAddedAtCoordinates(self, shipCoordinates):
        for coord in shipCoordinates:
            x = coord[0]
            y = coord[1]
            if not self.Exists(x, y) or not self.IsEmpty(x, y) or self.HaveNeighbours(x, y):
                return False
        return True

    def GetShipCoords(self, upperLeftX, upperLeftY, masts, direction):
        coords = []
        for i in range(masts):
            if(direction == "horizontal"):
                coords.append([upperLeftX + i, upperLeftY])
            else:
                coords.append([upperLeftX, upperLeftY + i])
        return coords

    def AddShipToBoard(self, ship):
        self.leftShips.append(ship)
        for coord in ship.coordinates:
            self.SetIdAtCoord(coord[0], coord[1], ship.id)

    def CheckIfAnyShipExists(self):
        if self.leftShips:
            return 1
        return 0

    def IfHit(self, coordinates):
        tmpId = self.GetIdAtCoord(coordinates[0], coordinates[1])
        #checks if coordId is ship
        if(tmpId != None):
            return self.IsDestroyed(tmpId)
        return 0

    def IsDestroyed(self, shipId):
        if self.IfCoordinatesAreAvailable(self.GetCoordinatesAtId(shipId)):
            #shipHit, but not destroyed
            return 1
        else:
            #shipDestroyed
            self.ShipDestroyed(next(x for x in self.leftShips if (x).id == shipId))
            return 2

    def IfCoordinatesAreAvailable(self, shipCoord):
        for val in shipCoord:
            if val in self.availableCoordinates:
                #if any coordinates of this ship are available
                return 1
        return 0

    def GetCoordinatesAtId(self, shipId):
        #returns coordinates of Ship with this id
        return (next(x for x in self.leftShips if (x).id == shipId)).GetCoordinates()

    def ShipDestroyed(self, ship):
        self.leftShips.remove(ship)

    def Shot(self, coordinates):
        self.availableCoordinates.remove(coordinates)
        return self.IfHit(coordinates)

    def SetIdAtCoord(self, x, y, id):
        self.idsGrid[y][x] = id

    def GetIdAtCoord(self, x, y):
        return self.idsGrid[y][x]

    def Exists(self, x, y):
        return x >= 0 and x < self.boardSize and y >= 0 and y < self.boardSize

    def IsEmpty(self, x, y):
        return self.GetIdAtCoord(x, y) is None

    def HaveNeighbours(self, x, y):
        possibleNeighbours = []
        for i in range(x-1, x+2):
            for j in range (y-1, y+2):
                if not self.Exists(i, j) or (i == x and j == y):
                    continue
                if not self.IsEmpty(i, j):
                    return True
        return False

    def GetAvailableCoordinates(self):
        return self.availableCoordinates