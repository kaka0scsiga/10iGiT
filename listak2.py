lista = [1,2,3]
print(type(lista))

lista2 = [1,2,3]
print(lista == lista2)

lista2 = list()
for x in lista:
    lista2.append(x)
print("lista2= ",lista2)
print(lista == lista2)

lista2 = [2,1,3]
print(lista == lista2)

lista = [1,"alma",2,True,lista2]
print(lista)
lista.apennd(lista)
print(lista)
print("_"*lista)
for x in lista:
    print(x)
    
print(lista[5])
print(lista[5][5])
print(lista[5][5][5])
print(lista[5][5][5][5])

del lista
#print(lista)


lista=list()
for i in range(0,10):
    
    lista.append(random,randint(1,1000))
print(lista)

del lista(1)
print(lista)

lista.pop()
print(lista)

x = lista.pop()
print(lista)

lista2 = lista.copy()
print(lista2)
    
lista.sort()
print(lista2)

lista2.reverse()
print(lista2)

lista.clear()
print(lista)

print(len(lista))

i = 1
for x in lista:
    print(i,xsep=", ")
    i +=1
print("-"*20)
for x in range(len(lista)):
    print(x,lista[x],sep=", ")
    print("-"*20)
    [print(x,lista[x],sep=", ") for x in range(len(lista))]

     