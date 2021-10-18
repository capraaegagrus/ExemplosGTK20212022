class Punto:
    """Clase que define a un punto en un plano de dúas dimensións"""
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Circulo (Punto):
    def __init__(self, x, y, r):
        Punto.__init__ (self,x,y)
        self.r = r

class Punto2:
    """Clase que representa puntos no primeiro cuarante
    Implica que x>0 e y>0
    """

    def __init__(self, x, y):
        self.x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        if x>0:
            self.__x = x
        else:
            raise ValueError
            #self.__x = 0
            #print ("O valor é inicializado a cero")

    def setY(self, y):
        if y>0:
            self.__y = y
        else:
            self.__y = 0
            print ("O valor é inicializado a cero")

    def __eq__(self, outro):
        if self.x == outro.x and self.y == outro.y:
            return True
        else:
            return False

    x = property (getX, setX)
    y = property (getY, setY)




p = Punto (1,3)
c = Circulo (2,3,6)
try:
    p2 = Punto2 (-3,5)
except ValueError:
    print ("Non se introducir valores que non sexan do 1º cadrante")

print (p.x)
print (c.x)
print (p2.getX())
#print (p2.__getY())
print (p2._Punto2__x)
#print (p2._Punto2__getY())

p2.x = 10

print (p2.x)
cadea = p2.__str__()
print (cadea)

'''
__init__(self, args)
__new__(cls, args)
__del__ (self)
__str__(self)
__cmp__(self, outro)

'''
print (p2.__eq__(p))
print (p2 == p)
print (p2.__sizeof__())

# Excepcións
try:
    print (5/0)
except (ZeroDivisionError, SyntaxError):
    print ("Erro: Non se pode facer división por cero")
except ValueError:
    print ("Erro: Valores incorrectos")
else:
    print ("A división realizouse correctamente")
finally:
    print ("A división fíxose ou non")