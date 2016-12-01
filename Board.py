class Board:
    leftShips = []
    availableCoordinates = []
    shots = []

    def __init__(self):
        print("Board created")
        ''' Something like this in loop:
        self.availableCoordinates.append([])
        self.availableCoordinates[0] = [1, 2]
        '''

    def CreateBoard(self):
        print("Create board here")

    def DrawShips(self):
        print("Draw ships here (random)")

    def AddShipsToBoard(self):
        print("Add drawed ships to board")

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