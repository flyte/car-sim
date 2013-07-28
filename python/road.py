class Road(object):

    def __init__(self, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        
    def can_go(self, direction):
        direction = direction.lower()
        if direction == "north" and self.north:
            return True
        elif direction == "east" and self.east:
            return True
        elif direction == "south" and self.south:
            return True
        elif direction == "west" and self.west:
            return True
        else:
            return False
