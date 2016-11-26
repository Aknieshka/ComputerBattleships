from Board import Board

class Player:
    id = None
    #state, that tells if previously player hit once or more
    move = None

    def __init__(self):
        print("Player created")

    def RandomShot(self):
        print("Create here mechanism of random shot")

    def FirstHit(self, x, y):
        #creates possibilities for shots
        tmpPossibilities = self.CreatePossibilities(x, y)
        Board.availableCoordinates.append([])
        Board.availableCoordinates.append([])
        Board.availableCoordinates[0] = [1,2]
        Board.availableCoordinates[1] = [3, 2]

        for item in list(tmpPossibilities):
            if(item not in Board.availableCoordinates):
                tmpPossibilities.remove(item)
        print(tmpPossibilities)
        #print("Create here mechanism when first hit")

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

