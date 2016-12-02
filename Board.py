import random

import Ship


class Board:
    boardSize = 10
    shipSizes = [4, 3, 2, 1]
    numOfShips = [1, 2, 3, 4]

    def __init__(self):
        self.leftShips = []
        self.availableCoordinates = []
        self.shots = []
        self.idsGrid = None

        print("Board created")
        ''' Something like this in loop:
        self.availableCoordinates.append([])
        self.availableCoordinates[0] = [1, 2]
        '''
        self.idsGrid = [[None for i in range(self.boardSize)] for i in range(self.boardSize)]
        self.CreateBoard()

    def CreateBoard(self):
        id = 0
        for i in range(len(self.shipSizes)):
            masts = self.shipSizes[i]
            for j in range(self.numOfShips[i]):
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
        print("ADDING SHIP: ", ship.coordinates)
        self.leftShips.append(ship)
        for coord in ship.coordinates:
            self.SetIdAtCoord(coord[0], coord[1], ship.id)
        self.PrintBoard()

    def CheckIfAnyShipExists(self):
        if self.leftShips:
            return 1
        return 0

    def IfHit(self):
        print("Check if hit")

    def ShipDestroyed(self):
        print("Handle ship destroyed")

    def Shot(self, coordinates):
        print("Create mechanism of shotting to coordinates, inform about result")
        #gets array of coordinates, e.g. [1,2]
        #return 0 - missed, change player?
        #return 1 - hit, but not destroyed
        #return 2 - hit and destroyed

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

    def PrintBoard(self):
        for x in range(self.boardSize):
            row = []
            for y in range(self.boardSize):
                if self.idsGrid[y][x] is None:
                    row.append("-")
                else:
                    row.append(str(self.GetIdAtCoord(x, y)))
            print(row)