#Paso de funcións como parámetros

def saudar (lingua):

    def saudar_es ():
        print ("Hola")

    def saudar_gl ():
        print ("Ola")

    def saudar_en ():
        print ("Hi")

    def saudar_fr ():
        print ("Salut")

    funcion_saudar ={
        "es": saudar_es,
        "en": saudar_en,
        "fr": saudar_fr,
        "gl": saudar_gl
    }

    return funcion_saudar[lingua]


f = saudar ("gl")
f()

saudar ("fr")()

#Funcións Lambda

def suma (x, y):
    return x + y

s = lambda x, y: x + y

print (suma (3, 2))
print (s(3,2))

def funcion2  (x, y, z=1):
    return (x + y)*z

z = lambda x, y, z = 1 : (x+y)*z

print (z (5,6,2))

l =[1,4,5,3,2,8,0]
c =['a', 'b']

def cadrado (n):
    return n**2

l2 = map (lambda n: n**2, l)
l3 = map (cadrado, l)
for n in l2:
    print (n)

#Compresión de listas
l2 = [n**2 for n in l]
l3 = [n for n in l if n % 2.0 == 0]
print (l3)

l4 = [s*v for s in c
          for v in l
          if v > 0]
print (l4)