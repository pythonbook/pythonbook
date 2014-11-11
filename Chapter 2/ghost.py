class Ghost(object):
    
    def __init__(self,color,x,y):
        self._color = color
        self._x = x
        self._y = y

    def change_color(self,color):
        self._color = color

    def print_position(self):
        print("x: " + str(self._x) + " y: " + str(self._y)) 
    
    def move_up(self):
        self._y += 1

