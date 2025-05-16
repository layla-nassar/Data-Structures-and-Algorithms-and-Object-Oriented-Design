class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y
    def __eq__(self, other):
        '''This function will return true if self and other have the same x and y attributes.'''
        if self.x == other.x and self.y == other.y:
            return True
        else: 
            return False
    def equidistant(self, other):
        '''This function returns true if self and other are the same distance from the origin.'''
        if ((self.x**2 +  self.y**2)**1/2) == ((other.x**2+  other.y**2)**1/2):
            return True
        else: 
            return False
    def within(self, distance, other):
        '''This function returns true if self and other are within distance from each other.'''
        if ((((other.x - self.x)**2) + ((other.y - self.y)**2))**(1/2)) <= distance:
            return True
        else:
            return False