
l = [1,2,3,4,5,6,7,8,9,10,112,113]

l2 = [1, "Dous", 3+4j,2.34, [1,2,3]]

print (l[2])
print (l2[1])
print (l[-2])
print (l2[-1][2])
print (l2[1][1])
print (l2[2])

l [2] = 15.9999

print (l)

print ( l[1:4])
print (l[1:-1:3])
print (l[1::2])
print (l[:6])
l[2:5] = ["Tres", "Catro","Cinco"]
print (l)
l[2:5] = ["Cero"]
print (l)

l3 = list()
l4 = []
l4.append (0)
l3.append (1)

t = 1,2, "Tres", [4,5,2+4j]
print (t)
t2 = 2,
print (t2)
print (t [3])
t[3][1] = 9
print (t)

for elemento in t:
    print (elemento)

#Diccionarios

d ={ 1: "Un",
     2: "Dous",
     3: "Tres",
     "Manuel": "25255345J"}
print (d[1])
print (d["Manuel"])
d["Manuel"] = "08051982"
print (d["Manuel"])

print (d.items())
print (d.keys())
print (d.values())
print (d.get ("Manuela", "Clave non encontrada"))

