class Ship:

    def __init__(self, id, masts, direction, upperLeftCoords):
        self.id = id
        self.masts = masts
        self.coordinates = []
        self.CreateCoordinates(masts, direction, upperLeftCoords)

    def CreateCoordinates(self, masts, direction, upperLeftCoords):
        upperLeftX = upperLeftCoords[0]
        upperLeftY = upperLeftCoords[1]
        for i in range(masts):
            if(direction == "horizontal"):
                self.coordinates.append([upperLeftX + i, upperLeftY])
            else:
                self.coordinates.append([upperLeftX, upperLeftY + i])

    def GetCoordinates(self):
        return self.coordinates