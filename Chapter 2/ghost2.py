class GhostBase(object):
    
    def __init__(self,color,x,y):
        self._color = color
        self._x = x
        self._y = y
	
    def change_color(self,color):
        self._color = color

    def print_position(self):
        print("x: " + str(self._x) + " y: " + str(self._y)) 


class GhostA(GhostBase):

    def __init__(self,color,x,y):
        GhostBase.__init__(self,color,x,y)
        self._color = color
        self._x = x
        self._y = y
    
    def move_up(self):
        self._y += 2
        
class GhostB(GhostBase):

    def __init__(self,color):
        GhostBase.__init__(self,color,2,2)
        self._color = color
        self._x = 2
        self._y = 2
        
    def move_up(self):
        self._y += 5
