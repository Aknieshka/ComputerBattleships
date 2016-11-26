class Ship:
    id = None
    masts = None
    coordinates = []

    def __init__(self):
        print("Ship created")

    def IsShotDown(self):
        print("Check if ship is shot down")

    def CreateCoordinates(self, masts, direction):
        print("Create here coordinates depending on masts and vertical/horizontal direction")