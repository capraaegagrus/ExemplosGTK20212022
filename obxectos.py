class Punto:
    """Clase que define a un punto en un plano de dúas dimensións"""
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Circulo (Punto):
    def __init__(self, x, y, r):
        Punto.__init__ (self,x,y)
        self.r = r




p = Punto (1,3)
c = Circulo (2,3,6)

print (p.x)
print (c.x)