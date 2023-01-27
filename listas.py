import os

os.system("cls")

def main(lista=None, msg = None):

    imprimirMenu() 

    if lista is None:
        try:
            opt = int(input("Seleccione una opción: "))
            validarOpcion(opt)

        except Exception as e:
            print("No es un número")
            main()
    else:
        try:
            opt = int(input("Seleccione una opción: "))
            validarOpcion(opt, lista)

        except Exception as e:
            print("No es un número")
            main(lista)

def imprimirMenu(msg = None): 
    os.system("cls")
    print("----Menu----\n 1) Crear lista\n 2) Añadir elemento\n 3) Eliminar elemento\n 4) Modificar elemento\n 5) Mostrar datos\n 6) Mostrar datos de forma inversa\n 7) Limpiar lista\n 8) Borrar lista")
    if msg != None:
        print(msg)

def validarOpcion(opt, lista=None):
    if opt == 1 and lista==None:
        lista = crearLista()
        main(lista)
    elif opt == 2 and list != None:
        lista = addElement(lista)
        main(lista)
    elif opt == 3 and list != None:
        lista = removeElement(lista)
        main(lista)
    elif opt == 4 and list != None:
        lista = updateElement(lista)
        main(lista)
    elif opt == 5 and list != None:
        print(lista)
        main(lista)
    elif opt == 6 and list != None:
        print(lista.reverse())
        main(lista)
    elif opt == 7 and list != None:
        lista = []
        main(lista)
    elif opt == 8 and list != None:
        lista = None
        main(lista)
           
def crearLista():
    lista_nueva = []
    imprimirMenu()
    return lista_nueva

def addElement(lista):
    element = input("Escribe el elemento a añadir: ")
    lista.append(element)
    return lista 

def removeElement(lista):
    print("Tu lista: ", lista)
    element = input("Escribe el elemento a eliminar: ")
    if element in lista:
        lista.remove(element)
        return lista
    else: 
        print("El elemento no se encuentra en la lista")
        removeElement(lista)

def updateElement(lista):
    print("Tu lista: ", lista)
    element = input("Escribe el elemento a actualizar: ")
    if element in lista:
        index = lista.index(element)
        lista[index] = input("Nuevo valor: ")
        return lista
    else: 
        print("El elemento no se encuentra en la lista")
        updateElement(lista)


main()