# Ejercicio 1

def RevisarRepetidos(Lista:list):
    Conjunto = set(Lista)
    if len(Lista) == len(Conjunto):
        print("No existen elemento repetidos")
    else:
        print("Si existen elementos repetidos")




#Ejercicio 2

def DosOMasBocales(Lista:list):
    for i in Lista:
        s = 0
        x = list(i)
        for i2 in x:
            if "a" == i2:
                s+=1
            elif "e" == i2:
                s+=1
            elif "i" == i2:
                s+=1 
            elif "o" == i2:
                s+=1
            elif "u" == i2:
                s+=1
        else:
            if s > 1:
                print(i)
            else:
                print(f"La palabra \"{i}\" no tiene dos o mas vocales") 





# Ejercicio 3

def QueNoTiene(Lista1:list, Lista2:list):
    Lista1.sort()
    ListaElemntosQNoTiene = []
    if Lista1 == Lista2:
        print("Las dos listas son iguales")
    else:
        for i in range(len(Lista1)):
            if Lista1[i] in Lista2:
                pass
            else:
                ListaElemntosQNoTiene.append(Lista1[i])
        print(f"los elementos que tine la lista 1 pero no la lista 2 son {ListaElemntosQNoTiene}")





# Ejercicio 4

def PromedioDeArreglos(Lista:list):
    Suma = 0
    for x in Lista:
        Suma += x
    return f" el promedio es {Suma/len(Lista)}"





# Ejercicio 5

def MedianaDeUnaLista(Lista:list):
    Lista.sort()
    if len(Lista) % 2 == 0:
        x = len(Lista)/2
        x = int(x)
        Suma = Lista[x-1] + Lista[x]
        return f" la mediana de la lista es {Suma/2}"
    else:
        x = (len(Lista) - 1)/2
        x = int(x)
        return f" la mediana de la lista es {Lista[x]}"
    


