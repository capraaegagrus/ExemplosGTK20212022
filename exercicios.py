'''Exercicio 6.2.1'''

def insertarCaracter (caracter, palabra):
    cadena = str()
    if len(palabra)==1:
        return palabra
    else:
        cadena = palabra[0:1] + ',' + insertarCaracter(caracter, palabra[1:])
        return cadena
        


'''Exercicio 6.2.2'''
def reemprazarEspazos (caracter, palabra):
    novaCadea = palabra.replace (' ', caracter)
    return novaCadea

print (reemprazarEspazos('*', "Bos días, como está vostede"))


'''Exercicio 6.2.3'''

def reemprazarDixitos (dixito, cadea):
    novaCadea = str()
    for i in range (0,len(cadea)):
        novaCadea = novaCadea + dixito
    return novaCadea

print (reemprazarDixitos ('X', "Segredo"))


'''Exercicio 6.6'''

def reemprazoVogal (palabra):
    """ordeV = {1:'a',
             2:'e',
             3:'i',
             4:'o',
             5:'u'}"""
    vogais ="aeiou"
    ordeV = { 'a':1,
              'e':2,
              'i':3,
              'o':4,
              'u':5}
    novaPalabra = list()
    for i in range (len (palabra)):
        caracter = palabra[i]
        if caracter in ordeV.keys():
            if ordeV[caracter] == 5 :
                novaPalabra[i] = vogais[0]
            else:
                novaPalabra.append(vogais[ordeV[caracter]])
        else:
            novaPalabra.append(caracter)
    return str(novaPalabra)

print (reemprazoVogal ("frigorifico"))



''''Exercicio 7.1'''

def elementosOrdeadosMenorMaior (t):
    ordeados = True
    if len (t) > 1:
        for i in range( 0,len(t)-2):
            if t[i]>t[i+1]:
                ordeados = False
                break
    return ordeados

tupla = (1,2,3,4,8,6,7)

print (elementosOrdeadosMenorMaior(tupla))


'''Exercicio 7.2.1'''

def fichasDominoEncaixanTuplas (ficha1, ficha2):
    encaixan = False

    if ficha1[0] == ficha2[0]:
        encaixan = True
    elif ficha1[0] == ficha2[1]:
        encaixan = True
    elif ficha1 [1] == ficha2 [0]:
        encaixan = True
    elif ficha1 [1] == ficha2 [1]:
        encaixan = True

    return encaixan

'''Exercicio 7.2.2'''

def fichasDominoEncaixanCadea (fichasCadea):

    fichas = fichasCadea.split()
    ficha1 = fichas[0].split ('-')
    ficha2 = fichas[1].split ('-')
    return fichasDominoEncaixanTuplas(ficha1, ficha2)

print (fichasDominoEncaixanTuplas((3,5), (2,5)))
print (fichasDominoEncaixanCadea('3-5 2-5'))

'''Exercicio 8.2.1'''

def vecesQueAparecenAsPalabras (frase):
    diccionario = dict()
    palabras = frase.split()
    for palabra in palabras:
        if palabra.lower() in diccionario:
            diccionario[palabra.lower()] = diccionario[palabra.lower()]+1
        else:
            diccionario[palabra.lower()] = 1
    return diccionario

print (vecesQueAparecenAsPalabras("Que bonito dia fai hoxe, pese a que chove"))

'''Exercicio 8.4'''

def cadeaLongaPorCaracteresEnTexto (texto):
    d = dict()
    palabras = texto.split()
    for i in range (len(texto)):
        caracter = texto[i]
        if caracter != ' ':
            if not caracter in d:
                for palabra in palabras:
                    if palabra.count (caracter) != 0:
                        if caracter in d:
                            if len(d[caracter]) < len (palabra):
                                d [caracter] = palabra
                        else:
                            d [caracter] = palabra
    return d

print (cadeaLongaPorCaracteresEnTexto("A  estaba oscuro e paixaxe fúnebre"))







